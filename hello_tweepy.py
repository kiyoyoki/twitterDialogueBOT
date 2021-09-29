# Tweepyを用いてAPIから「Hello world!」とtweetを行うプログラム
import os
import tweepy
from dotenv import load_dotenv

load_dotenv('./.env')
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.environ.get('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API obj
api = tweepy.API(auth)

# tweet
api.update_status("Hello world!")