# mandarin-twitter-bot
To never forget to tweet for Mandarin class.


### Start
1. Use pip to install the dependencies in **requirements.txt** <br>
2. Request a [Twitter developer account](https://developer.twitter.com) if you don't have one <br>
3. [Create a Twitter app and obtain your API Keys](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app) 
4. Copy this and add your API keys in a new Python file **credentials.py** <br>
    ```python
    consumer_key        = 'your_key_here'
    consumer_secret     = 'your_key_here'
    access_token        = 'your_key_here'
    access_token_secret = 'your_key_here'
    ```
5. Clone this repository to your computer <br>
6. Navigate to the project directory <br>
7. Run `python bot.py` in the terminal (or run from a development environment) <br> 

### Adjustments
* This program takes a set of pre-written tweets from input.txt, separated by a newline <br>
* Enter desired tweets in **input.txt** <br>
* Go to **bot.py** and change `time.sleep()` in the for loop to your desired interval. The default is one tweet per 24hrs. <br>


[Tweepy](http://www.tweepy.org) handles OAuth and Tweeting functionality. <br>
Here are the [Tweepy Docs](https://tweepy.readthedocs.io/en/latest/api.html#API.home_timeline) <br>
