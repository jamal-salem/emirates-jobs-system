from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:

    with engine.connect() as connection:

        jobs = connection.execute(text("SELECT * FROM jobs")).fetchall()
        candidates = connection.execute(text("SELECT * FROM candidates")).fetchall()

        print("\n=== MATCH RESULTS ===\n")

        for candidate in candidates:

            for job in jobs:

                score = 0

                job_text = f"{job.title} {job.company} {job.location}".lower()

                preferred_sector = candidate.preferred_sector.lower()
                skills = candidate.skills.lower()

                keywords = [
                    "police",
                    "military",
                    "government",
                    "security",
                    "emergency",
                    "response"
                ]

                for keyword in keywords:

                    if keyword in preferred_sector:
                        if keyword in job_text:
                            score += 1

                    if keyword in skills:
                        if keyword in job_text:
                            score += 1

                if score > 0:

                    print(f"Candidate: {candidate.full_name}")
                    print(f"Job: {job.title}")
                    print(f"Company: {job.company}")
                    print(f"Match Score: {score}")
                    print("-" * 40)

except Exception as e:
    print("Error:")
    print(e)
