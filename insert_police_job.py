from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

insert_query = """
INSERT INTO jobs (
    title,
    company,
    location,
    source,
    apply_link
)

VALUES (

    'ADP Emergency Security Response',
    'Abu Dhabi Police',
    'Abu Dhabi',
    'AD Police Portal',
    'https://ers.adpolice.gov.ae'
);
"""

try:
    with engine.connect() as connection:
        connection.execute(text(insert_query))
        connection.commit()

    print("Police job inserted successfully!")

except Exception as e:
    print("Error:")
    print(e)
