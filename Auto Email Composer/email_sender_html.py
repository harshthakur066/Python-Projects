import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from pathlib import Path
from string import Template

load_dotenv()

# get your email and password and make sure that Less secure app access is on for your acount

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Professor'
email['to'] = 'harshthakur066@gmail.com'
email['subject'] = 'Testing for auto mail'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(email)
    print('ALl good!')
