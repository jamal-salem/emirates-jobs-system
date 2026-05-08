from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

create_table_query = """

CREATE TABLE IF NOT EXISTS job_sources (

    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    url TEXT,
    source_type VARCHAR(255),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

"""

try:

    with engine.connect() as connection:

        connection.execute(text(create_table_query))
        connection.commit()

    print("Job sources table created successfully!")

except Exception as e:
    print("Error:")
    print(e)
