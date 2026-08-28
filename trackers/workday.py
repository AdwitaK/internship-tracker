import requests
from urllib.parse import urlparse
from trackers.base_tracker import BaseTracker


class WorkdayTracker(BaseTracker):

    def fetch_jobs(self, company):
        careers_url = company["identifier"]

        # Parse careers URL
        parsed = urlparse(careers_url)

        host = parsed.netloc
        path_parts = parsed.path.strip("/").split("/")

        tenant = host.split(".")[0]

        #Handle different URL formats
        if len(path_parts) >= 2:
            locale = path_parts[0]
            site = path_parts[1]
            base_url = f"{parsed.scheme}://{host}/{locale}/{site}"

        elif len(path_parts) == 1:
            locale = None
            site = path_parts[0]
            base_url = f"{parsed.scheme}://{host}/{site}"

        else:
            raise ValueError(
                f"Unexpected Workday URL format: {careers_url}"
            )

        url = f"https://{host}/wday/cxs/{tenant}/{site}/jobs"

        jobs = []
        offset = 0
        limit = 20
        total = None

        while total is None or offset < total:
            payload = {
                "appliedFacets": {},
                "limit": limit,
                "offset": offset,
                "searchText": ""
            }

            response = requests.post(url, json=payload)
            response.raise_for_status()

            data = response.json()
            
            if total is None:
                total = data["total"]

            postings = data["jobPostings"]

            for job in postings:
                external_path = job.get("externalPath")

                jobs.append({
                    "job_id": external_path or "Unknown",
                    "company": company["company"],
                    "title": job.get("title", "Unknown"),
                    "location": job.get("locationsText", "Unknown"),
                    "url" : f"{base_url}{external_path}" if external_path else "Unknown"
                })

            offset+=limit

        return jobs