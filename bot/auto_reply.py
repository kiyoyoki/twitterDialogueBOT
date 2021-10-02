# twitterDialogueBOT/bot/auto_reply.py

import tweepy
from config import create_api
import time
import random

def check_mentions(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            # 自身のタイムラインにあるとダメみたい(Tweetを削除するとOK)
            # tweepy.errors.Forbidden: 403 Forbidden　187 - Status is a duplicate.
            # ↑のエラーは再起動時に、一度Tweetした内容と同じ文言(status)は二度と使用できない模様
            api.update_status(
                status="Hello",
                in_reply_to_status_id=tweet.id, # リプライ対象のTweetID
                auto_populate_reply_metadata=True, # Trueにすることで@usernameの形式になる
            )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["test"], since_id)
        # 定期Tweetを以下のようにランダムに行っても、内容が被った瞬間に以下のエラーが出る
        # どうやらスパム防止で同内容を連投できない仕様になっているそうな
        # tweepy.errors.Forbidden: 403 Forbidden　187 - Status is a duplicate.
        # 現在時刻をTweetに埋め込むことで対処可能ではある。
        api.update_status(random.choice(['こんにちは!', 'ヤッホー!', 'みんな元気?']) + "\n" + time.ctime())
        time.sleep(60)

if __name__ == "__main__":
    main()