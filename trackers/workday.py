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
        site = path_parts[-1]

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
                jobs.append({
                    "job_id": job["bulletFields"],
                    "company": company["company"],
                    "title": job["title"],
                    "location": job["locationsText"],
                    "url": f"{parsed.scheme}://{host}{job['externalPath']}"
                })

            offset+=limit

        return jobs