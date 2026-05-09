from flask import Flask, render_template
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.route("/")
def home():

    with engine.connect() as connection:

        total_candidates = connection.execute(
            text("SELECT COUNT(*) FROM candidates")
        ).scalar()

        total_jobs = connection.execute(
            text("SELECT COUNT(*) FROM jobs")
        ).scalar()

        total_matches = total_candidates * total_jobs

    return render_template(

        "dashboard.html",

        total_candidates=total_candidates,

        total_jobs=total_jobs,

        total_matches=total_matches

    )


@app.route("/candidates")
def candidates():

    query = "SELECT * FROM candidates"

    with engine.connect() as connection:

        result = connection.execute(text(query)).fetchall()

    return render_template(
        "candidates.html",
        candidates=result
    )


@app.route("/jobs")
def jobs():

    query = "SELECT * FROM jobs"

    with engine.connect() as connection:

        result = connection.execute(text(query)).fetchall()

    return render_template(
        "jobs.html",
        jobs=result
    )


@app.route("/matches")
def matches():

    matches_data = []

    with engine.connect() as connection:

        jobs = connection.execute(
            text("SELECT * FROM jobs")
        ).fetchall()

        candidates = connection.execute(
            text("SELECT * FROM candidates")
        ).fetchall()

        for candidate in candidates:

            for job in jobs:

                score = 0

                job_text = f"""
                {job.title}
                {job.company}
                {job.location}
                """.lower()

                candidate_text = f"""
                {candidate.skills}
                {candidate.preferred_sector}
                {candidate.specialization}
                """.lower()

                keywords = [

                    "police",
                    "military",
                    "government",
                    "security",
                    "linux",
                    "network",
                    "cybersecurity",
                    "emergency",
                    "response",
                    "it support"

                ]

                for keyword in keywords:

                    if keyword in candidate_text:

                        if keyword in job_text:

                            score += 1

                if score > 0:

                    matches_data.append({

                        "candidate": candidate.full_name,
                        "job": job.title,
                        "company": job.company,
                        "score": score

                    })

    return render_template(
        "matches.html",
        matches=matches_data
    )


if __name__ == "__main__":

    app.run(debug=True)
