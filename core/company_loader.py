import csv

def load_companies(filepath="data/companies.csv"):
    companies = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            companies.append({
                "company": row["Company"].strip(),
                "priority": int(row["Priority"]),
                "ats": row["ATS"].strip().lower(),
                "identifier": row["Identifier"].strip()
            })
    return companies