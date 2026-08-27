import json
import os


def load_seen_jobs(filepath="data/seen_jobs.json"):

    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_seen_jobs(seen_jobs, filepath="data/seen_jobs.json"):

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(seen_jobs, file, indent=4)