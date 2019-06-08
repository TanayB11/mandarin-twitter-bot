# mandarin-twitter-bot
To never forget to tweet for Mandarin class.


### Start
Use pip to install the dependencies in **requirements.txt** <br>
Request a [Twitter developer account](https://developer.twitter.com) if you don't have one. <br>
[Obtain your API Keys](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app) and declare them in a new Python file **credentials.py** <br>
Clone this repository to your computer <br>
Navigate to the project directory <br>
Run `python bot.py` in the terminal (or run from a development environment) <br> 

### Adjustments
This program takes a set of pre-written tweets from input.txt, separated by a newline. <br>
Enter desired tweets in **input.txt** <br>
Go to **bot.py** and change `time.sleep()` in the for loop to your desired interval. The default is one tweet per 24hrs. <br>


[Tweepy](http://www.tweepy.org) handles OAuth and Tweeting functionality. <br>
Here are the [Tweepy Docs](https://tweepy.readthedocs.io/en/latest/api.html#API.home_timeline) <br>
