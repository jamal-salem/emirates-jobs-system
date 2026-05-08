from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM candidates;"

try:

    with engine.connect() as connection:

        result = connection.execute(text(query))

        print("\n=== CANDIDATES ===\n")

        for row in result:

            print(f"ID: {row.id}")
            print(f"Name: {row.full_name}")
            print(f"Specialization: {row.specialization}")
            print(f"City: {row.city}")
            print(f"Preferred Sector: {row.preferred_sector}")
            print(f"Skills: {row.skills}")
            print(f"Languages: {row.languages}")
            print("-" * 50)

except Exception as e:
    print("Error:")
    print(e)
