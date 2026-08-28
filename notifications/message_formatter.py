def build_messages(jobs):

    if not jobs:
        return None
    
    messages = []
    current_message = "New internships found\n\n"

    for job in jobs:

        job_text = (
            f"**{job['company']}**\n"
            f"{job['title']}\n"
            f"{job['location']}\n"
            f"<{job['url']}>\n\n"
        )

        if len(current_message) + len(job_text) > 1900:
            messages.append(current_message)
            current_message = ""

        current_message += job_text

    if current_message:
        messages.append(current_message)

    return messages