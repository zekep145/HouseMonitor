from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC718dd16e6b94bf8b0fd27c2109b51015"
# Your Auth Token from twilio.com/console
auth_token  = "aabfee7826edcb280c3d6ecdf10a8418"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12072400694",
    from_="+19199483470",
    body="Hello from Python!",
    media_url='https://img00.deviantart.net/d7b7/i/2016/155/c/5/blastoise_pixel_art__not_the_best__by_gavinsoap-da51a19.png')

print(message.sid)