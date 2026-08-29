import requests
from trackers.base_tracker import BaseTracker

class SmartRecruitersTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://api.smartrecruiters.com/v1/companies/{identifier}/postings"
    
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()

        jobs = []

        for job in data["content"]:
            job_response = requests.get(job["ref"])
            ref = job.get("ref")

            if ref:
                job_response = requests.get(ref)
                job_response.raise_for_status()
                job_data = job_response.json()
                posting_url = job_data.get("postingUrl", "Unknown")
            else:
                posting_url = "Unknown"

            jobs.append({
                "job_id": str(job.get("id", "Unknown")),
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": job.get("name", "Unknown"),
                "location": job.get("location", {}).get("city", "Unknown"),
                "url": posting_url
            })

        return jobs