import requests
from trackers.base_tracker import BaseTracker

class BambooHRTracker(BaseTracker):

    def fetch_jobs(self, company):
        identifier = company["identifier"]

        url = f"https://{identifier}.bamboohr.com/careers/list"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data["result"]:
            #get location
            location = job.get("location") or {}
            ats_location = job.get("atsLocation") or {}

            location_string = ", ".join(
                part for part in [
                    location.get("city"),
                    location.get("state")
                ]
                if part
            )

            if not location_string:
                location_string = ", ".join(
                    part for part in [
                        ats_location.get("city"),
                        ats_location.get("state"),
                        ats_location.get("province"),
                        ats_location.get("country")
                    ]
                    if part
                )

            if not location_string:
                location_string = "Unknown"

            #get job id + url
            job_id = str(job.get("id", "Unknown"))

            if job_id != "Unknown":
                posting_url = f"https://{identifier}.bamboohr.com/careers/{job_id}"
            else:
                posting_url = "Unknown"

            #build job
            jobs.append({
                "job_id": job_id,
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": job.get("jobOpeningName", "Unknown"),
                "location": location_string,
                "url": posting_url
            })

        return jobs