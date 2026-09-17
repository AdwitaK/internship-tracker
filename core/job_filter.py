INTERNSHIP_KEYWORDS = [
    "intern",
    "internship",
    "co-op",
    "coop",
    "student",
    "university",
    "undergraduate"
]

EXCLUDE_KEYWORDS = [
    "senior",
    "principal",
    "manager",
    "director",
    "lead",
    "2026", 
    "internal",
    "phd",
    "ph.d",
    "electrical",
    "mechanical",
    "manufacturing",
    "civil",
    "chemical",
    "winter",
    "chemical",
    "environmental",
    "industrial",
    " graduate"
]

TECH_KEYWORDS = [
    "software",
    "developer",
    "development",
    "data", 
    "engineering",
    "engineer",
    "machine learning",
    "ml ",
    "ai ",
    "artificial intelligence",
    "robotics",
    "perception",
    "computer vision",
    "cv ",
    "vision",
    "autonomy",
    "autonomous",
    "embedded",
    "firmware",
    "backend",
    "frontend",
    "full stack",
    "full-stack",
    "platform",
    "data",
    "simulation",
    "controls",
    "systems",
    "research",
    "researcher"
]

EXCLUDE_LOCATIONS = [
    "china",
    "taiwan",
    "singapore",
    "poland",
    "germany",
    "london",
    "amsterdam",
    "netherlands",
    "argentina",
    "mexico",
    "australia",
    "hong kong",
    "bristol",
    "paris",
    "france",
    "belgrade",
    "auckland",
    "nz",
    "new zealand",
    "egypt",
    "italy",
    "switzerland",
    "india",
    "gurgaon",
    "norway",
    "israel",
    "tianjin",
    "ireland",
    "united kingdom",
    "brazil",
    "malaysia",
    "qatar",
    "dublin",
    "vietnam"
]

def is_relevant(job):

    title = str(job.get("title", "")).lower()
    location = str(job.get("location", "")).lower()

    has_include = any(
        keyword in title
        for keyword in INTERNSHIP_KEYWORDS
    )

    has_exclude = any(
        keyword in title
        for keyword in EXCLUDE_KEYWORDS
    )

    is_tech = any(
        keyword in title
        for keyword in TECH_KEYWORDS
    )

    has_exclude_location = any(
        keyword in location
        for keyword in EXCLUDE_LOCATIONS
    )

    return has_include and is_tech and not has_exclude and not has_exclude_location