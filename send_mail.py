import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject, body, recipients):
    # Get sender's email address and password from environment variables
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')
    if not sender_email or not sender_password:
        raise ValueError("Sender's email address or password is not set in environment variables.")
    print(sender_email, sender_password)
    # Construct the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())

def main():
    # Read recipients from the text file
    with open('recipients.txt', 'r') as file:
        recipients = [line.strip() for line in file if line.strip()]

    subject = "Testing envitonment variables"
    body = "Hello friends, This is email generated using python script on github, run through Jenkins. For authentication of mail server, it is using environment variables."

    send_email(subject, body, recipients)

if __name__ == "__main__":
    main()
