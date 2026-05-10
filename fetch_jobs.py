import requests

from sqlalchemy import create_engine, text

from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

url = "https://remotive.com/api/remote-jobs"

response = requests.get(url)

data = response.json()

jobs = data["jobs"]

print("\n=== FETCHING JOBS ===\n")

with engine.connect() as connection:

    for job in jobs[:20]:

        title = job["title"]

        company = job["company_name"]

        location = "Remote"

        source = "Remotive API"

        job_url = job["url"]

        category = job["category"]

        remote = "Yes"

        insert_query = text("""

        INSERT INTO jobs

        (

            title,
            company,
            location,
            source,
            url,
            category,
            remote

        )

        VALUES

        (

            :title,
            :company,
            :location,
            :source,
            :url,
            :category,
            :remote

        )

        """)

        connection.execute(

            insert_query,

            {

                "title": title,

                "company": company,

                "location": location,

                "source": source,

                "url": job_url,

                "category": category,

                "remote": remote

            }

        )

        print(f"Inserted: {title}")

    connection.commit()

print("\nDONE!")
