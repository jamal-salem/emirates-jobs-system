from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM jobs;"

try:
    with engine.connect() as connection:
        result = connection.execute(text(query))

        print("\n=== JOBS ===\n")

        for row in result:
            print(f"ID: {row.id}")
            print(f"Title: {row.title}")
            print(f"Company: {row.company}")
            print(f"Location: {row.location}")
            print(f"Source: {row.source}")
            print(f"Apply Link: {row.apply_link}")
            print("-" * 40)

except Exception as e:
    print("Error:")
    print(e)
