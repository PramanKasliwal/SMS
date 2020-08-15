from twilio.rest import Client

account_sid = '<your-sid>'
auth_token = '<your-token>'
client = Client(account_sid, auth_token)
to = input("Send message to: <Eg: +919876543210> ")
msg = input("Message: <Press 'enter' to send>\n")

message = client.messages.create(
                              body=msg,
                              from_='<selected-mobile-number>',
                              to=to
                          )
print("Message sent successfully!")