from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

insert_query = """
INSERT INTO jobs (title, company, location, source, apply_link)
VALUES (
    'Network Support Technician',
    'Al Ain Tech',
    'Al Ain',
    'Manual Entry',
    'https://example.com/job2'
);
"""

try:
    with engine.connect() as connection:
        connection.execute(text(insert_query))
        connection.commit()

    print("Job inserted successfully!")

except Exception as e:
    print("Error:")
    print(e)
