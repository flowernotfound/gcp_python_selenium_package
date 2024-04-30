import smtplib
from email.mime.text import MIMEText
import os

MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

def send_error_email(error_message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'thnksfrth3244@gmail.com'
    sender_password = MAIL_PASSWORD
    recipient_email = 'thnksfrth3244@gmail.com'

    subject = 'エラー通知: ねっぱんデータ取得'
    body = f"ねっぱんのスクリプトの実行中にエラーが発生しました。\n\nエラー内容:\n{error_message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
