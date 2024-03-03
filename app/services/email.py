from flask import current_app
from flask_mail import Message
from app import mail


def send_email(recipients, subject, text_body=None, html_body=None):
    msg = Message(
        subject=subject,
        sender=(current_app.config["MAIL_USERNAME"]),
        recipients=recipients,
        body=text_body,
        html=html_body,
    )
    mail.send(msg)
