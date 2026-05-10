from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

allowed_keywords = [

    "uae",
    "dubai",
    "abu dhabi",
    "sharjah",
    "al ain",
    "ajman",
    "ras al khaimah",
    "fujairah"

]

with engine.connect() as connection:

    jobs = connection.execute(
        text("SELECT id, location FROM jobs")
    ).fetchall()

    for job in jobs:

        location = str(job.location).lower()

        valid = False

        for keyword in allowed_keywords:

            if keyword in location:

                valid = True

        if not valid:

            delete_query = text("""

            DELETE FROM jobs
            WHERE id = :id

            """)

            connection.execute(

                delete_query,

                {"id": job.id}

            )

            print(f"Deleted Job ID: {job.id}")

    connection.commit()

print("\nUAE jobs filter complete!")
