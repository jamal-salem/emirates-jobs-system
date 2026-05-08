from flask import Flask, render_template
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.route("/")
def home():

    return """
    <h1>Emirates Jobs System 🔥</h1>
    <p>System is running successfully</p>
    <a href='/candidates'>View Candidates</a>
    """

@app.route("/candidates")
def candidates():

    query = "SELECT * FROM candidates"

    with engine.connect() as connection:

        result = connection.execute(text(query)).fetchall()

    return render_template(
        "candidates.html",
        candidates=result
    )

if __name__ == "__main__":

    app.run(debug=True)
