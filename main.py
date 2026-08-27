from core.company_loader import load_companies
from trackers.tracker_map import TRACKER_MAP

def main():
    companies = load_companies()

    for company in companies:
        #to be removed eventually
        if(company["ats"] != "workable" and company["ats"] != "greenhouse" and company["ats"] != "ashbyhq" and company["ats"] != "lever"):
            continue
        
        tracker_class = TRACKER_MAP[company["ats"]]
        tracker = tracker_class()

        jobs = tracker.fetch_jobs(company)

        print(f"Company: {company["company"]}, {len(jobs)} jobs")

        '''for job in jobs[:5]:
            print(f"  - {job['title']}")
            print(f"    {job['location']}")
            print(f"    {job['url']}")'''

if __name__ == "__main__":
    main()