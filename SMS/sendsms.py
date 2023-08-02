from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    body="hello kingpin",
    from_= keys.twilio_number,
    to=keys.phone_no  # phone number verified in twilio
)
