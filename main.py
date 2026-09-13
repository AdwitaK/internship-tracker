from core.company_loader import load_companies
from trackers.tracker_map import TRACKER_MAP
from core.seen_jobs import load_seen_jobs
from core.seen_jobs import save_seen_jobs
from core.job_filter import is_relevant
from notifications.discord_notifier import DiscordNotifier
from notifications.message_formatter import build_messages
import os
from dotenv import load_dotenv
import traceback

def main():
    companies = load_companies()
    seen_jobs = load_seen_jobs()
    new_jobs = []

    for company in companies:
        print("Checking company ", company["company"]) #test
        #Skip custom ats systems
        if(company["ats"] == "custom"):
            continue

        # Instantiate correct ATS Tracker class
        tracker_class = TRACKER_MAP[company["ats"]]

        ## Guard against missing ats
        if tracker_class is None:
            print(
                f"Unknown ATS: {company['ats']} "
                f"for {company['company']}"
            )
            continue

        tracker = tracker_class()

        # Fetch jobs from ATS, skip if error occurs
        try:
            jobs = tracker.fetch_jobs(company)
        except Exception as e:
            print(
                f"Failed: {company['company']} "
                f"({company['ats']})"
            )
            print(e)
            traceback.print_exc()
            continue

        # Process fetched jobs
        for job in jobs:

            ## skip malformed jobs
            if not job["job_id"]:
                continue

            ## skip all jobs seen before
            job_key = f"{job['company']}:{job['job_id']}"

            if job_key in seen_jobs:
                continue

            ## add newly found job to seen regardless of relevance
            seen_jobs[job_key] = {
                "title": job["title"]
            }

            ## check job relevance
            if not is_relevant(job):
                continue

            ## add to new jobs only if relevant
            new_jobs.append(job)

    save_seen_jobs(seen_jobs)

    # Send notification
    if new_jobs:
        load_dotenv()
        notifier = DiscordNotifier(os.getenv("DISCORD_WEBHOOK"))
        messages = build_messages(new_jobs)
        for message in messages:
            notifier.send(message)

    #Testing
    for job in new_jobs:
        print(f"{job["company"]} : {job["title"]} ")


if __name__ == "__main__":
    main()