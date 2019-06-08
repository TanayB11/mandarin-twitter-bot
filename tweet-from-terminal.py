# This program is inside a venv.
# Run $ 'python -m idlelib' to launch with access to dependencies
# Run start() to start tweeting once a day from all tweets in input.txt

# Import all API credentials
from credentials import *
import tweepy

# From Tweepy docs
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
        
def tweetText(line):
    if line != '\n':
        print(line)
        api.update_status(line) # This actually posts the tweet - text only

line = input('Enter your tweet: ')
tweetText(line)
