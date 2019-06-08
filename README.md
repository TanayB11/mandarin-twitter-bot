# mandarin-twitter-bot
To never forget to tweet for Mandarin class.


## Start
Use pip to install the dependencies in requirements.txt
Request a [Twitter developer account]https://developer.twitter.com if you don't have one.
[Obtain your API Keys]https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app and declare them in a new Python file **credentials.py**
Clone this repository to your computer
Navigate to the project directory
Run `python bot.py` in the terminal (or run from a development environment)

## Adjustments
This program takes a set of pre-written tweets from input.txt, separated by a newline. Enter desired tweets in **input.txt**
Go to **bot.py** and change `time.sleep()` in the for loop to your desired interval. The default is one tweet per 24hrs.


[Tweepy]http://www.tweepy.org handles OAuth and Tweeting functionality.
Here are the [Tweepy Docs]https://tweepy.readthedocs.io/en/latest/api.html#API.home_timeline
