# twitterbot_textfile.py
"""This model provides functions for connecting to twitter, tweeting a tweet, and tweeting every hour"""
from credentials import *
import tweepy
from time import sleep
from generator_functions import *
from model import *
from random import randrange


def connection_twitter(tweet):
    """Access and authorize our Twitter credentials from credentials module,
    update twitter status with the tweet supplied as argument"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.update_status(tweet)

        print(tweet)

    except tweepy.TweepError as e:
        print(e.reason)


def tweet_an_hour(tweets):
    """Access and authorize our Twitter credentials from credentials module
    tweet a new tweet every hour"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    number = randrange(0, len(tweets))
    tweet = tweets[number]

    try:
        api.update_status(tweet)

        print(tweet)
        sleep(3600)

    except tweepy.TweepError as e:
        print(e.reason)
