import smtplib

from email.mime.text import MIMEText

from dotenv import load_dotenv

import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")

EMAIL_PASS = os.getenv("EMAIL_PASS")

subject = "Smart Recruit Test"

body = """

Hello Jamal,

Your UAE Recruitment Platform
is working successfully 🚀

"""

msg = MIMEText(body)

msg["Subject"] = subject

msg["From"] = EMAIL_USER

msg["To"] = EMAIL_USER

server = smtplib.SMTP(

    "smtp.mail.yahoo.com",
    587

)

server.starttls()

server.login(

    EMAIL_USER,
    EMAIL_PASS

)

server.send_message(msg)

server.quit()

print("\nEmail Sent Successfully!")
