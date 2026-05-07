from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

insert_query = """
INSERT INTO candidates (
    full_name,
    email,
    phone,
    specialization,
    city,
    skills,
    preferred_sector,
    cv_path
)

VALUES (

    'Mohammed Musabbeh Salem Abdulla Alshamsi',
    'malshm@icloud.com',
    '+971502877737',
    'Firefighter / Emergency Response',
    'Al Ain',
    'Emergency Response, Firefighting, Rescue Operations, Computer Skills, Leadership, Communication',
    'Police / Military / Government',
    '/cv/mohammed_alshamsi_cv.pdf'
);
"""

try:
    with engine.connect() as connection:
        connection.execute(text(insert_query))
        connection.commit()

    print("Candidate inserted successfully!")

except Exception as e:
    print("Error:")
    print(e)
