import tweepy as tw
import os

access_token_key = os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']
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