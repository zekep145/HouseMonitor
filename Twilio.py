from twilio.rest import Client
from configparser import ConfigParser


class Twilio:

    def __init__(self):
        config = ConfigParser()
        config.read('static/twilio.ini')

        # Your Account SID from twilio.com/console
        self.account_sid = config.get('config', 'account_sid')
        # Your Auth Token from twilio.com/console
        self.auth_token  = config.get('config', 'auth_token')
        # Number to send text to
        self.number_to = config.get('config','number_to')
        # Twilio number sent from
        self.number_from = config.get('config', 'number_from')

        print("Twilio object created using the following \n"
              "account_sid: {0} \n"
              "auth_token: {1}".format(self.account_sid, self.auth_token))
        print("Creating messages from {0} to {1}".format(self.number_from, self.number_to))

    def send_message(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            to=self.number_to,
            from_=self.number_from,
            body="Hello from Python!",
            media_url='https://img00.deviantart.net/d7b7/i/2016/155/c/5/blastoise_pixel_art__not_the_best__by_gavinsoap-da51a19.png')

        print(message.sid)
