import tweepy
from config import Config


class TwitterManager():
    def __init__(self):
        config = Config()
        auth = tweepy.OAuthHandler(
            str(config.api_key),
            str(config.api_key_secret),
        )
        auth.set_access_token(
            str(config.access_token),
            str(config.access_token_secret),
        )
        self.twitter = tweepy.API(auth)

    def send_tweet(self, status):
        print("test")
        self.twitter.update_status(
            status=status,
        )
