from collections import Counter

def build_messages(jobs):

    if not jobs:
        return None

    PRIORITY_LABELS = {
        1: "🔥 PRIORITY 1",
        2: "⭐ PRIORITY 2",
        3: "📌 PRIORITY 3",
        4: "📄 PRIORITY 4",
        5: "👀 WATCH LIST"
    }

    jobs.sort(key=lambda job: (job["priority"], job["company"],job["title"]))
    priority_counts = Counter(
        job["priority"] for job in jobs
    )

    summary = (
    f"🔥 {priority_counts.get(1, 0)}   "
    f"⭐ {priority_counts.get(2, 0)}   "
    f"📌 {priority_counts.get(3, 0)}   "
    f"📄 {priority_counts.get(4, 0)}   "
    f"👀 {priority_counts.get(5, 0)}"
    )

    messages = []
    current_message = (
    f"{len(jobs)} new internships found\n\n"
    f"{summary}\n"
    )  
    
    current_priority = None

    for job in jobs:

        # Add a Priority header whenever job priority changes
        if job["priority"] != current_priority:
            count = priority_counts[job["priority"]]

            header = (
                f"\n{'━' * 20}\n"
                f"{PRIORITY_LABELS.get(job['priority'], 'OTHER')} ({count})\n"
                f"{'━' * 20}\n\n"
            )

            if len(current_message) + len(header) > 1900:
                messages.append(current_message)
                current_message = ""

            current_message += header
            current_priority = job["priority"]

        # Add job details
        job_text = (
            f"**{job['company']}**\n"
            f"{job['title']}\n"
            f"{job['location']}\n"
            f"<{job['url']}>\n\n"
        )

        if len(current_message) + len(job_text) > 1900:
            messages.append(current_message)
            current_message = ""

            ## Re-add sections header after message split
            current_message += (
                f"{PRIORITY_LABELS.get(job['priority'], 'OTHER')} ({count})\n\n"
            )

        current_message += job_text

    if current_message:
        messages.append(current_message)

    return messages