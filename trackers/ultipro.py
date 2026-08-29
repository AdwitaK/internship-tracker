import requests
from trackers.base_tracker import BaseTracker


class UltiproTracker(BaseTracker):

    def fetch_jobs(self, company):

        url = company["identifier"]
        search_url = url + "JobBoardView/LoadSearchResults"
        jobs = []

        top = 50
        skip = 0
        total = None

        while total is None or skip < total:

            payload = {
                "opportunitySearch": {
                    "Top": top,
                    "Skip": skip,
                    "QueryString": ""
                },
                "matchCriteria": {
                    "PreferredJobs": [],
                    "Educations": [],
                    "LicenseAndCertifications": [],
                    "Skills": [],
                    "hasNoLicenses": False
                }
            }

            response = requests.post(search_url, json=payload)
            response.raise_for_status()

            data = response.json()

            if total is None:
                
                total = data["totalCount"]

            for job in data["opportunities"]:
                jobId = job.get("Id", "Unknown")

                jobs.append({
                    "job_id": jobId,
                    "company": company["company"],
                    "priority": int(company["priority"]),
                    "title": job.get("Title", "Unknown"),
                    "location": (
                        job.get("Locations", [{}])[0]
                        .get("Address", {})
                        .get("City", "Unknown")
                    ),
                    "url": (url + "OpportunityDetail?opportunityId=" + jobId 
                            if jobId != "Unknown" 
                            else jobId)
                })

            skip += top

        return jobs