# twitterDialogueBOT/bot/config.py
# this module authenticate to the Twitter API
import tweepy
import os

def create_api():
    TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
    TWITTER_API_SECRET_KEY = os.environ.get('TWITTER_API_SECRET_KEY')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    # Authenticate to Twitter
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)
    
    return api