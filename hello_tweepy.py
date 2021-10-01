# Tweepyを用いてAPIから「Hello world!」とtweetを行うプログラム
import os
from posix import times_result
import tweepy

"""
A status is a tweet.
A friendship is a follow-follower relationship.
A favorite is a like.

Tweepy’s functionality can be divided into the following groups

OAuth：OAuth認証に関わる機能

The API class：Twitter API endpointsへアクセスする機能
Methods for user timelines
Methods for tweets
Methods for users
Methods for followers
Methods for your account
Methods for likes
Methods for blocking users
Methods for searches
Methods for trends
Methods for streaming

Models

Cursors
Streams
"""

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
# Twitter DevelopersのApp permissions
# Write許可していなかったせいで、原因解決にだいぶ時間かかった。
# api.update_status("Hello world!")

# 自身のタイムライン取得(デフォルトは最新20status)
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")