import tweepy as tw
import os

# consumer_key = 'EddqPzmNlCmUCQBPf7aLlg7pi'
# consumer_secret = 'ishRiJYIr99ko8ojtJHtcJyXxsr4Q5le5GmJ1LW0gEGewCujRy'
# access_token_key = '139177787-oCipscf6pImkxaxxZ9EyT4g1DwckqxsP5jPaJPU7'
# access_token_secret = 'cmxnZXcnjp6uts78yoP1BaNUuEJUVvbY3ZGZF5efemp4w'

access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['HOMaccess_token_secretE']
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
Bearer_token = os.environ['Bearer_token']

client = tw.Client(consumer_key=consumer_key,
                   consumer_secret=consumer_secret,
                   access_token_secret=access_token_secret,
                   access_token=access_token_key)

auth = tw.OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret)
auth.set_access_token(key=access_token_key,secret=access_token_secret)
api = tw.API(auth)