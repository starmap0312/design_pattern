import smtplib, subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "Sender Name <sender@example.com>"
RECIPIENT = "Recipient Name <receiver@example.com>"
SUBJECT = "subject"
PLAIN_CONTENT = "plain text"
HTML_CONTENT = "<html><p>html text</p></html>"
SERVER = "relayserver.example.com"

# configure the message
msg = MIMEMultipart('alternative')
msg['Subject'] = SUBJECT
msg['From'] = SENDER
msg['To'] = RECIPIENT # can be a list of addresses

# attach parts of two MIME types: text/plain and text/html
part1 = MIMEText(PLAIN_CONTENT, 'plain')
part2 = MIMEText(HTML_CONTENT, 'html')
msg.attach(part1)
msg.attach(part2)

# send the mail
smtp = smtplib.SMTP(SEVER)
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()
