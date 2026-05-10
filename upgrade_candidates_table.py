from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

queries = [

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS email TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS github TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS linkedin TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS preferred_role TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS preferred_location TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS work_type TEXT

    """,

    """

    ALTER TABLE candidates
    ADD COLUMN IF NOT EXISTS experience_level TEXT

    """

]

with engine.connect() as connection:

    for query in queries:

        connection.execute(text(query))

        print("Executed Successfully")

    connection.commit()

print("\nCandidates table upgraded!")
