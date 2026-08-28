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

            print(response.url)
            data = response.json()

            if total is None:
                
                total = data["totalCount"]

            for job in data["opportunities"]:

                jobs.append({
                    "job_id": job["Id"],
                    "company": company["company"],
                    "title": job["Title"],
                    "location": job["Locations"][0]["Address"]["City"],
                    "url": url + "OpportunityDetail?opportunityId=" + job["Id"]
                })

            skip += top

        return jobs