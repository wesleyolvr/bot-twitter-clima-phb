import tweepy as tw

# consumer_key = 'EddqPzmNlCmUCQBPf7aLlg7pi'
# consumer_secret = 'ishRiJYIr99ko8ojtJHtcJyXxsr4Q5le5GmJ1LW0gEGewCujRy'
# access_token_key = '139177787-oCipscf6pImkxaxxZ9EyT4g1DwckqxsP5jPaJPU7'
# access_token_secret = 'cmxnZXcnjp6uts78yoP1BaNUuEJUVvbY3ZGZF5efemp4w'

access_token_key = '1478385643717865482-U2WncYCeatc0oRm0DV0mCPwlHgOaeM'
access_token_secret = 'tENizxT3GXqcMsYwiZd8D1nsjhih2WALD2BDmkwlEvdab'
consumer_key = 'nV6VvejJvZ3WPGgJgxoMYZTXc'
consumer_secret = 'EZ06GR8EtcITLGFlmpTQe0APFvYCD2DSP1wnYm50jXNLAaOUEu'
Bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHQEXwEAAAAAXV2CPmCRxVIEld5ueBNBWOuVU%2Fs%3DMWyJ13tvyuhf3Q1A1j3SLIvZvtwmDHsH2s4xeo5Gnb96dFS90k'

client = tw.Client(consumer_key=consumer_key,
                   consumer_secret=consumer_secret,
                   access_token_secret=access_token_secret,
                   access_token=access_token_key)

auth = tw.OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret)
auth.set_access_token(key=access_token_key,secret=access_token_secret)
api = tw.API(auth)