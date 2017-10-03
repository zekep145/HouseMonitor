from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="",
    from_="",
    body="Hello from Python!",
    media_url='https://img00.deviantart.net/d7b7/i/2016/155/c/5/blastoise_pixel_art__not_the_best__by_gavinsoap-da51a19.png')

print(message.sid)
