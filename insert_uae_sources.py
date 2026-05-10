from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sources = [

    {

        "name": "Bayt UAE",

        "url": "https://www.bayt.com/ar/uae/jobs/",

        "type": "Job Board"

    },

    {

        "name": "Naukrigulf UAE",

        "url": "https://arabic.naukrigulf.com/jobs-in-uae",

        "type": "Job Board"

    },

    {

        "name": "Dubai Careers",

        "url": "https://dubaicareers.ae/ar/pages/default.aspx",

        "type": "Government"

    },

    {

        "name": "Emirates Group Careers",

        "url": "https://www.emiratesgroupcareers.com/information-technology/",

        "type": "Corporate"

    },

    {

        "name": "Dubizzle UAE Jobs",

        "url": "https://uae.dubizzle.com/ar/jobs/",

        "type": "Marketplace"

    },

    {

        "name": "Waseet UAE Jobs",

        "url": "https://ae.waseet.net/ar/landing/195-jobs",

        "type": "Marketplace"

    }

]

with engine.connect() as connection:

    for source in sources:

        insert_query = text("""

        INSERT INTO sources

        (name, url, type)

        VALUES

        (:name, :url, :type)

        """)

        connection.execute(

            insert_query,

            {

                "name": source["name"],

                "url": source["url"],

                "type": source["type"]

            }

        )

        print(f"Inserted: {source['name']}")

    connection.commit()

print("\nUAE Sources Added Successfully!")
