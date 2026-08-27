import requests
from trackers.base_tracker import BaseTracker

class LeverTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://api.lever.co/v0/postings/{company['identifier']}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data:
            jobs.append({
                "job_id": str(job["id"]),
                "company": company["company"],
                "title": job["text"],
                "location": job["categories"]["location"],
                "url": job["hostedUrl"]
            })

        return jobs