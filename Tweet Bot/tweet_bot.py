import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except (tweepy.RateLimitError, StopIteration):
        time.sleep(300)


# folower bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'HIMANSHU KUMAR MAURYA':
        follower.follow()
        break

search_string = 'JavaScript'
num = 2

# like or retweet bot
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(num)):
    try:
        tweet.favorite()  # tweet.retweet()
        print('I liked it')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
