from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

insert_query = """

INSERT INTO job_sources (

    name,
    url,
    source_type

)

VALUES (

    'Abu Dhabi Police',
    'https://ers.adpolice.gov.ae',
    'Police'

);

"""

try:

    with engine.connect() as connection:

        connection.execute(text(insert_query))
        connection.commit()

    print("Source inserted successfully!")

except Exception as e:
    print("Error:")
    print(e)
