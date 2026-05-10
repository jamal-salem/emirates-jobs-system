from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

queries = [

    """

    ALTER TABLE jobs
    ADD COLUMN IF NOT EXISTS source TEXT

    """,

    """

    ALTER TABLE jobs
    ADD COLUMN IF NOT EXISTS url TEXT

    """,

    """

    ALTER TABLE jobs
    ADD COLUMN IF NOT EXISTS category TEXT

    """,

    """

    ALTER TABLE jobs
    ADD COLUMN IF NOT EXISTS remote TEXT

    """

]

with engine.connect() as connection:

    for query in queries:

        connection.execute(text(query))

        print("Executed successfully")

    connection.commit()

print("\nJobs table updated!")
