import requests
from trackers.base_tracker import BaseTracker

class GreenhouseTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://boards-api.greenhouse.io/v1/boards/{identifier}/jobs"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data["jobs"]:
            jobs.append({
                "job_id": str(job.get("id", "Unknown")),
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": job.get("title", "Unknown"),
                "location": job.get("location", {}).get("name", "Unknown"),
                "url": job.get("absolute_url", "Unknown")
            })

        return jobs

