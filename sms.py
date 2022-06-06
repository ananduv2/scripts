from twilio.rest import Client
account_sid = ["ACeec51f4dc8366e8129909e402cfff945"]
auth_token = ["4e498899238ca0501dbece1f50b3cacb"]
client = Client(account_sid, auth_token)
message = client.messages.create(body='Hi there! How are you?', from_=[FROM_NUM, to=[VERIFIED_NUMBER])
print(message.sid)