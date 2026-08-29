import requests
from trackers.base_tracker import BaseTracker

class GemTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://api.gem.com/job_board/v0/{identifier}/job_posts/"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data:
            jobs.append({
                "job_id": str(job.get("id", "Unknown")),
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": job.get("title", "Unknown"),
                "location": job.get("location", {}).get("name", "Unknown"),
                "url": job.get("absolute_url", "Unknown")
            })

        return jobs