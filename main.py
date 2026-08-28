from core.company_loader import load_companies
from trackers.tracker_map import TRACKER_MAP
from core.seen_jobs import load_seen_jobs
from core.seen_jobs import save_seen_jobs
from core.job_filter import is_relevant
from notifications.discord_notifier import DiscordNotifier
from notifications.message_formatter import format_jobs
import os
from dotenv import load_dotenv

def main():
    companies = load_companies()
    seen_jobs = load_seen_jobs()
    new_jobs = []

    for company in companies[:1]:

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
            continue

        # Process fetched jobs
        for job in jobs:

            ## skip malformed jobs
            if not job["job_id"]:
                continue

            ## skip all jobs seen before
            if job["job_id"] in seen_jobs:
                continue

            ## add newly found job to seen regardless of relevance
            seen_jobs[job["job_id"]] = {
                "company": job["company"],
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
        #print(os.getenv("DISCORD_WEBHOOK"))
        notifier = DiscordNotifier(os.getenv("DISCORD_WEBHOOK"))
        message = format_jobs(new_jobs)
        notifier.send(message)
        print("message sent!") #test

    #Testing
    print(len(new_jobs))
    for job in new_jobs:
        print(f"{job["company"]} : {job["title"]} ")


if __name__ == "__main__":
    main()