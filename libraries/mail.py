import smtplib, subprocess
from email.mime.text import MIMEText

SENDER = "sender@example.com"
RECEIVER = "receiver@example.com"

# configure the message
msg = MIMEText("<body>content</body>", 'html')
msg['Subject'] = "title"
msg['From'] = SENDER
msg['To'] = RECEIVER

# send the mail
client = smtplib.SMTP("relayserver.example.com")
client.sendmail(SENDER, [RECEIVER], msg.as_string())
client.quit()
