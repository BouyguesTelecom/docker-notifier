import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import html2text

class MailNotifier:
    def notification_type(self):
        return "Mail"

    def send(self, title, message):
        mail_from = os.environ.get("MAIL_FROM")
        rcpt_to = os.environ.get("MAIL_TO")

        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = mail_from
        msg['To'] = rcpt_to

        text = html2text.html2text(message)
        html = message

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP(os.environ.get("SMTP_HOST"), port=int(os.environ.get("SMTP_PORT", "25")))
        s.sendmail(mail_from, rcpt_to, msg.as_string())
        s.quit()