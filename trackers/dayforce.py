import requests
from trackers.base_tracker import BaseTracker

class DayforceTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = (f"https://www.dayforcehcm.com/api/{identifier}/V1/JobFeeds")

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data:
            location = ", ".join(
                part for part in [
                    job.get("City"),
                    job.get("State"),
                    job.get("Country")
                ]
                if part
            )

            jobs.append({
                "job_id": str(job.get("ReferenceNumber", "Unknown")),
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": job.get("Title", "Unknown"),
                "location": location or "Unknown",
                "url": job.get("JobDetailsUrl", "Unknown")
            })

        return jobs