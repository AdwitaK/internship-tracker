import requests
from trackers.base_tracker import BaseTracker

class AshbyTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://api.ashbyhq.com/posting-api/job-board/{company['identifier']}"

        response = requests.get(url)
        response.raise_for_status()
    
        data = response.json()
    
        jobs = []

        for job in data["jobs"]:
            jobs.append({
                "job_id": str(job.get("id", "Unknown")),
                "company": company["company"],
                "title": job.get("title", "Unknown"),
                "location": job.get("location", "Unknown"),
                "url": job.get("jobUrl", "Unknown")
            })

        return jobs
