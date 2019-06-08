# This program is inside a venv.
# Run $ 'python -m idlelib' to launch with access to dependencies
# Run start() to start tweeting once a day from all tweets in input.txt

# Import all API credentials
from credentials import *
import tweepy
import time

# From Tweepy docs
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open('input.txt', 'r') as txt_file:
    txt_lines = txt_file.readlines()
ctr = 0 # Number of tweets posted by bot

def tweetText(line):
    if line != '\n':
        print(line)
        api.update_status(line) # This actually posts the tweet - text only
        
def updateLog(line):
     with open('log.txt', 'w') as log_file:
        log_file.write('Number of tweets posted by bot: ' + str(ctr+1) + '\n')
        log_file.write('Latest tweet: ' + line + '\n')

for line in txt_lines:
    tweetText(line)
    updateLog(line)
    ctr+=1
    time.sleep(86400) # Sleep for one day

# Suggestion for improvement: Add support for modified files using date of modification
