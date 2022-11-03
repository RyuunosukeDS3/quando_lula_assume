import logging

from api import TwitterManager
from app import Scheduler, StatusCreator
from config import Config, config_logger

config_logger()
config = Config()
twitter_manager = TwitterManager()
scheduler = Scheduler()
status_creator = StatusCreator()


def send_tweet():
    status = status_creator.create_status_message()
    twitter_manager.send_tweet(status)

    logging.info("Tweet: %s sent.", status)


def start_seding_tweets():

    logging.info("Configuring scheduler to run at %s UTC", config.send_time)
    scheduler.schedule_everyday(config.send_time, send_tweet)


start_seding_tweets()
