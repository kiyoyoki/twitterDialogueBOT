# Tweepyを用いてAPIから「Hello world!」とtweetを行うプログラム
# v1.1 →　v2なので、そちらを使用したほうが良い?
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


# idを指定して、特定のアカウントのステータスを読み込む
"""
user = api.get_user(screen_name="sekine_kiyo")
print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
"""

# tweet検索
# Pythonが含まれる日本語の最新Tweetを10件取得
for tweet in api.search_tweets(q="Python", lang="en", result_type="recent", count=10):
    print(f"{tweet.user.name}:{tweet.text}\n")

# 他にもいろいろできる
# フォロー・プロフィール編集・いいね・ブロックユーザ表示etc...
