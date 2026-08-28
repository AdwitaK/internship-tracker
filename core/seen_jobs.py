import json
import os

SEEN_JOB_FILE = "data/seen_jobs.json"

def load_seen_jobs(filepath=SEEN_JOB_FILE):

    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_seen_jobs(seen_jobs, filepath=SEEN_JOB_FILE):

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(seen_jobs, file, indent=4)