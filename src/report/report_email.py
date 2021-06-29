import os
import smtplib, ssl

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_message(text):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Report test"
    message["From"] = os.environ.get("SENDER")
    message["To"] = os.environ.get("RECEIVER")
    # html = open("template.html", "r").read()
    # part2 = MIMEText(html, "html")
    part2 = MIMEText(text, "plain")
    message.attach(part2)
    return message


def send_email(text):
    load_dotenv()
    if os.environ.get("REPORT_THIS") == "True":
        message = create_message(text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(os.environ.get("SENDER"), os.environ.get("PASSWORD"))
            server.sendmail(
                os.environ.get("SENDER"), os.environ.get("RECEIVER"), message.as_string()
            )
