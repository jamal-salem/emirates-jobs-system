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
    cv_path,
    education,
    experience,
    certifications,
    languages

)

VALUES (

    'Jamal Salem',
    'jaudi990@yahoo.com',
    '+971543621874',
    'IT Support / Computer Engineering / Information Security',
    'Al Ain',
    
    'Windows, Linux, TCP/IP, Networking, IT Support, Troubleshooting, Data Handling, Virtual Machines, Python, Cybersecurity, C Programming',
    
    'Government / Police / IT / Cybersecurity',

    '/cv/jamal_salem_cv.pdf',

    'Masters Degree in Information Security Systems - Azerbaijan Technical University | Bachelor Degree in Computer Engineering - Azerbaijan Technical University',

    'Technical Support and Operations at Quick Parts UAE | Technical Support and Inspection at Unilux Industrial Company | Data Entry and IT Support at Travel and Tourism Agency Azerbaijan',

    'Google IT Support Professional Certificate | IT Support in Healthcare - Johns Hopkins | Cybersecurity Fundamentals IBM | UNICEF Security Risk Training | Google AI Infrastructure | Google Analytics Certification',

    'Arabic, English, Azerbaijani'

);
"""

try:

    with engine.connect() as connection:

        connection.execute(text(insert_query))
        connection.commit()

    print("Jamal profile inserted successfully!")

except Exception as e:
    print("Error:")
    print(e)
