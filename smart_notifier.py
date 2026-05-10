import smtplib

from email.mime.text import MIMEText

from sqlalchemy import create_engine, text

from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

EMAIL_USER = os.getenv("EMAIL_USER")

EMAIL_PASS = os.getenv("EMAIL_PASS")

engine = create_engine(DATABASE_URL)

keywords = [

    "it",
    "support",
    "network",
    "cybersecurity",
    "linux",
    "technical"

]

with engine.connect() as connection:

    jobs = connection.execute(
        text("SELECT * FROM jobs")
    ).fetchall()

    for job in jobs:

        already_sent = connection.execute(

            text("""

            SELECT * FROM sent_jobs
            WHERE job_id = :job_id

            """),

            {"job_id": job.id}

        ).fetchone()

        if already_sent:

            print(f"Already Sent: {job.title}")

            continue

        score = 0

        text_data = f"""

        {job.title}
        {job.company}
        {job.location}

        """.lower()

        for keyword in keywords:

            if keyword in text_data:

                score += 1

        if score >= 2:

            subject = f"New Matching Job: {job.title}"

            body = f"""

Hello Jamal,

A new matching UAE job was found.

Title:
{job.title}

Company:
{job.company}

Location:
{job.location}

Match Score:
{score}

Good luck 🚀

"""

            msg = MIMEText(body)

            msg["Subject"] = subject

            msg["From"] = EMAIL_USER

            msg["To"] = EMAIL_USER

            server = smtplib.SMTP_SSL(

                "smtp.mail.yahoo.com",
                465

            )

            server.login(

                EMAIL_USER,
                EMAIL_PASS

            )

            server.send_message(msg)

            server.quit()

            connection.execute(

                text("""

                INSERT INTO sent_jobs
                (job_id)

                VALUES (:job_id)

                """),

                {"job_id": job.id}

            )

            connection.commit()

            print(f"Email Sent: {job.title}")

print("\nDone!")
