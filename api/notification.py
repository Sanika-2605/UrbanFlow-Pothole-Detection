
# from twilio.rest import Client
# from django.core.mail import send_mail
# from django.conf import settings
# import os

# def send_sms(phone, message):
#     try:
#         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#         message = client.messages.create(
#             body=message,
#             from_=settings.TWILIO_PHONE_NUMBER,
#             to=phone
#         )
#         return True
#     except Exception as e:
#         print(f"Failed to send SMS: {e}")
#         return False

# def send_alert_email(to_email, subject, message):
#     send_mail(
#         subject,
#         message,
#         os.getenv("EMAIL_HOST_USER"),
#         [to_email],
#         fail_silently=False,
#     )






from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
import os
# Ensure that the Twilio client is properly configured with environment variables


def send_sms(phone, message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    sender = settings.TWILIO_PHONE_NUMBER
    message = client.messages.create(body=message, from_=sender, to=phone)
    return message.sid

def send_alert_email(to_email, subject, message):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])