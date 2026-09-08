
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
import datetime

## 01
Email = os.getenv("SENDER_EMAIL") # Sender email
Key = os.getenv("APP_PASSWORD")      # app password

## 02
reciver = ["jkunal121@gmail.com"]

## 03 
def make_message():       ##( to create the msg)
    mail = MIMEMultipart()
    mail['From'] = Email
    mail['To'] = ", ".join(reciver)
    mail['Subject'] = "Nikhil's Automated Report"

    ## 04                 ( to add the message into mail )
    body_text = f"Hello, this mail was sent at {datetime.datetime.now()}"
    mail.attach(MIMEText(body_text, 'plain'))

    ## 05   Attach the file 
    file_name = "report.pdf"
    try:
        with open(file_name, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={file_name}")
            mail.attach(part)
    except Exception as e:
        print("File not attached:", e)

    return mail

##  06   to send the email
def send_mail_now():
    message = make_message()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(Email, Key)

    for person in reciver:
        server.sendmail(Email, person, message.as_string())

    server.quit()
    print("Mail delivered successfully!")

send_mail_now()

## 07: Schedule the time for mail( when we want to repaer daily on specific time)
#schedule.every().day.at("09:00").do(send_mail_now)

## 08 keep it auto
#while True:
    #schedule.run_pending()
    #time.sleep(1)
