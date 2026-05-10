from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

query = """

CREATE TABLE IF NOT EXISTS sent_jobs (

    id SERIAL PRIMARY KEY,

    job_id INTEGER,

    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

"""

with engine.connect() as connection:

    connection.execute(text(query))

    connection.commit()

print("\nSent jobs table created!")
