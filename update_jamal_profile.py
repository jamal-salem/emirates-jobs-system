from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

update_query = """

UPDATE candidates

SET

email = :email,

github = :github,

linkedin = :linkedin,

preferred_role = :preferred_role,

preferred_location = :preferred_location,

work_type = :work_type,

experience_level = :experience_level

WHERE full_name = :full_name

"""

data = {

    "email": "jaudi990@yahoo.com",

    "github": "https://github.com/jamal-salem",

    "linkedin": "https://www.linkedin.com/in/jamal-salem-0030a7334/",

    "preferred_role": "IT Support, Technical Support, Cybersecurity, Networking",

    "preferred_location": "Al Ain, Abu Dhabi, UAE",

    "work_type": "Onsite / Hybrid / Remote",

    "experience_level": "Junior",

    "full_name": "Jamal Salem"

}

with engine.connect() as connection:

    connection.execute(

        text(update_query),

        data

    )

    connection.commit()

print("\nJamal profile updated successfully!")
