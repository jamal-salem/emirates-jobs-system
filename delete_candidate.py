from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

delete_query = """

DELETE FROM candidates
WHERE full_name = 'Mohammed Musabbeh Salem Abdulla Alshamsi'

"""

try:

    with engine.connect() as connection:

        connection.execute(text(delete_query))
        connection.commit()

    print("Candidate deleted successfully!")

except Exception as e:

    print("Error:")
    print(e)
