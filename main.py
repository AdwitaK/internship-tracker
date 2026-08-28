from core.company_loader import load_companies
from trackers.tracker_map import TRACKER_MAP

def main():
    companies = load_companies()

    for company in companies[:10]:
        if(company["ats"] == "custom"):
            continue

        tracker_class = TRACKER_MAP[company["ats"]]
        tracker = tracker_class()

        jobs = tracker.fetch_jobs(company)

        print(f"Company: {company["company"]}, {len(jobs)} jobs")


if __name__ == "__main__":
    main()