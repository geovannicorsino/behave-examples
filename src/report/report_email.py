import os
import smtplib, ssl
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_message():
    message = MIMEMultipart("alternative")
    message["Subject"] = "Report test"
    message["From"] = os.environ.get("SENDER")
    message["To"] = os.environ.get("RECEIVER")
    html = open("template.html", "r").read()
    part2 = MIMEText(html, "html")
    message.attach(part2)
    return message


def send_email():
    load_dotenv()
    if os.environ.get("REPORT_THIS") == "True":
        message = create_message()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(os.environ.get("SENDER"), os.environ.get("PASSWORD"))
            server.sendmail(
                os.environ.get("RECEIVER"), os.environ.get("RECEIVER"), message.as_string()
            )


send_email()
