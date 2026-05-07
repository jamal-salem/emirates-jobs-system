from sqlalchemy import create_engine

DATABASE_URL = "postgresql://jamal_app:jamal123@localhost/emirates_jobs"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Database connected successfully!")
    connection.close()
except Exception as e:
    print("Connection failed:")
    print(e)