from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://jamal_app:jamal123@localhost/emirates_jobs"

engine = create_engine(DATABASE_URL)

create_jobs_table = """
CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    source VARCHAR(255),
    apply_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_candidates_table = """
CREATE TABLE IF NOT EXISTS candidates (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    specialization VARCHAR(255),
    city VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

try:
    with engine.connect() as connection:
        connection.execute(text(create_jobs_table))
        connection.execute(text(create_candidates_table))
        connection.commit()

    print("Tables created successfully!")

except Exception as e:
    print("Error:")
    print(e)
