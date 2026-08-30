import requests
import xml.etree.ElementTree as ET

from urllib.parse import urlparse, parse_qs
from trackers.base_tracker import BaseTracker


class SuccessFactorsTracker(BaseTracker):

    def fetch_jobs(self, company):

        careers_url = company["identifier"]

        parsed = urlparse(careers_url)
        query_params = parse_qs(parsed.query)

        company_id = query_params.get("company", [None])[0]

        if not company_id:
            raise ValueError(f"Could not extract company parameter from {careers_url}")

        base_url = f"{parsed.scheme}://{parsed.netloc}"

        xml_url = (
            f"{base_url}/career"
            f"?company={company_id}"
            f"&career_ns=job_listing_summary"
            f"&resultType=XML"
        )

        response = requests.get(xml_url)
        response.raise_for_status()

        root = ET.fromstring(response.text)

        jobs = []

        for job in root.findall(".//Job"):

            title = job.findtext("JobTitle", "Unknown")
            job_id = job.findtext("ReqId", "Unknown")
            description = job.findtext("Job-Description", "")

            description_lower = description.lower()

            if any(keyword in description_lower for keyword in [
                "canada",
                "ontario",
                "quebec",
                "british columbia",
                "alberta"
            ]):
                location = "Canada"

            elif any(keyword in description_lower for keyword in [
                "usa",
                "united states",
                "united states of america"
            ]):
                location = "USA"

            else:
                location = "Unknown"

            jobs.append({
                "job_id": str(job_id),
                "company": company["company"],
                "priority": int(company["priority"]),
                "title": title,
                "location": location,
                "url": careers_url
            })

        return jobs