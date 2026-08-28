from core.company_loader import load_companies
from trackers.tracker_map import TRACKER_MAP
from core.seen_jobs import load_seen_jobs
from core.seen_jobs import save_seen_jobs

def main():
    companies = load_companies()
    seen_jobs = load_seen_jobs()
    new_jobs = []

    for company in companies[:1]:
        if(company["ats"] == "custom"):
            continue

        tracker_class = TRACKER_MAP[company["ats"]]
        tracker = tracker_class()

        jobs = tracker.fetch_jobs(company)

        for job in jobs:
            if job["job_id"] in seen_jobs:
                continue

            new_jobs.append(job)
            seen_jobs[job["job_id"]] = {
                "company": job["company"],
                "title": job["title"]
            }

        save_seen_jobs(seen_jobs)

        print(f"Company: {company["company"]}, {len(new_jobs)} new jobs")


if __name__ == "__main__":
    main()