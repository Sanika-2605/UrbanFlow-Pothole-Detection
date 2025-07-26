# api/utils/twilio_utils.py

# from twilio.rest import Client
# from django.conf import settings

# def send_sms(to_number, message):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         body=message,
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=to_number
#     )
#     return message.sid




# from twilio.rest import Client
# from django.conf import settings

# def send_sms(to_number, message):
#     account_sid = settings.TWILIO_ACCOUNT_SID
#     auth_token = settings.TWILIO_AUTH_TOKEN 

#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body=message,
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=to_number
#     )
#     return message.sid
   
from twilio.rest import Client
from django.conf import settings

# Initialize Twilio client
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# ✅ For OTP via Verification Service
def send_otp(phone):
    verification = client.verify.services(settings.TWILIO_VERIFY_SID).verifications.create(
        to=phone,
        channel='sms'
    )
    return verification.status

def verify_otp(phone, code):
    verification_check = client.verify.services(settings.TWILIO_VERIFY_SID).verification_checks.create(
        to=phone,
        code=code
    )
    return verification_check.status == 'approved'

# ✅ For sending generic SMS alerts (like pothole detection)
def send_sms(to_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"✅ SMS sent to {to_number}")
        return True
    except Exception as e:
        print(f"❌ Failed to send SMS to {to_number}: {e}")
        return False
