#twilio integration file

# Download the twilio-python library from http://twilio.com/docs/libraries
# pip install twilio should work, otherwise use easy_install twilio
import sys
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC93bc79a222d23f5e7e09308591e8bec2"
auth_token = "ceef4b2d00ddca1ddc4b73ede5bc4539"
client = TwilioRestClient(account_sid, auth_token)
#"+17654097348" shivam's # if needed
message = client.messages.create(to="+14088934962", from_="+14083421269",
                                     body="Testing send_sms.py at WildHacks 2016")