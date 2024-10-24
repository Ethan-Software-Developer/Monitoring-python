import smtplib
import requests
from email.mime.text import MIMEText
import time

# Email credentials
SENDER_EMAIL = 'ethansevenster621@gmail.com'  # Your Gmail address
SENDER_PASSWORD = 'Deadpool2006'        # Your Gmail password (or app password)
RECIPIENT_EMAIL = 'ethansevenster5@gmail.com'  # Recipient's email address

# Function to send email
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Email sent!")

# Function to check website status
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Website returned status code {response.status_code}")
        print(f"{url} is up.")
    except Exception as e:
        print(f"{url} is down! Error: {e}")
        send_email("Website Down Alert", f"Alert: {url} is down!")

if __name__ == "__main__":
    website_to_monitor = "https://example.com"  # Replace with the website you want to monitor

    while True:
        check_website(website_to_monitor)
        time.sleep(60)  # Check every 60 seconds
