from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

queries = [

"""
ALTER TABLE candidates
ADD COLUMN IF NOT EXISTS skills TEXT;
""",

"""
ALTER TABLE candidates
ADD COLUMN IF NOT EXISTS preferred_sector VARCHAR(255);
""",

"""
ALTER TABLE candidates
ADD COLUMN IF NOT EXISTS cv_path TEXT;
"""
]

try:
    with engine.connect() as connection:

        for query in queries:
            connection.execute(text(query))

        connection.commit()

    print("Candidates table updated successfully!")

except Exception as e:
    print("Error:")
    print(e)
