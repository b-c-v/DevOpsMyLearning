#!/bin/env python

import psutil
import smtplib
from email.mime.text import MIMEText

# pip install psutil

sender_email = ""
receiver_email = ""
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = ""
smtp_password = ""


def send_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Alert email send successfully!")
    except Exception as e:
        print(f"Failed to send email alert: {e}")


def monitor_system():
    try:
        cpu_threshold = 10
        memory_threshold = 10

        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        if cpu_usage > cpu_threshold:
            send_alert("Hight CPU usage", f"{cpu_usage}")

        if memory_usage > memory_threshold:
            send_alert("Hight memory usage", f"{memory_usage}")
    except Exception as e:
        print(f"An error occurred while monitoring: {e}")


monitor_system()
