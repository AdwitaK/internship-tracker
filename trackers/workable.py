import requests
from trackers.base_tracker import BaseTracker

class WorkableTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://apply.workable.com/api/v1/widget/accounts/{identifier}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data["jobs"]:
            jobs.append({
                "job_id": str(job["shortcode"]),
                "company": company["company"],
                "title": job["title"],
                "location": job["city"] + ", " + job["country"],
                "url": job["url"]
            })

        return jobs

