def format_jobs(jobs):

    if not jobs:
        return None

    lines = []

    lines.append(
        f"{len(jobs)} new internship(s) found\n"
    )

    for job in jobs:

        lines.append(
            f"**{job['company']}**"
        )

        lines.append(
            job["title"]
        )

        lines.append(
            job["location"]
        )

        lines.append(
            job["url"]
        )

        lines.append("")

    return "\n".join(lines)