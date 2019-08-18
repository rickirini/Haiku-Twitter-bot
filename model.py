# model.py
"""This module provides a Model class"""
from generator_functions import *
from twitterbot_textfile import *
from random import randrange


class Model:
    """This class stores the state of the program"""

    def __init__(self):
        """The init method initializes self.tweets as empty list"""
        self.tweets = []

    def generate(self):
        """The generate method generates a list of tweekus by using a generator
        imported from the generator_functions module, returns list"""
        self.tweets = accidental_haiku("tweets")
        return self.tweets

    def generate_random(self):
        """The generate random method generates a list of random tweekus
        by using a generator imported from the generator_functions module,
        returns list"""
        self.tweets = random_haiku("tweets")
        return self.tweets

    def retweet(self, tweet):
        """The retweet method retweets the tweet that was supplied as argument by
        using a method (connection_twitter) that was imported
        from the twitterbot_textfile module"""
        connection_twitter(tweet)
        return True

    def random_tweet(self, tweets):
        """returns a random tweet from the list of tweets supplied as argument"""
        number = randrange(0, len(tweets))
        tweet = tweets[number]
        return tweet

    def retweet_hour(self, tweets):
        """The retweet_hour method retweets a tweet every hour
        from the list supplied as argument"""
        tweet_an_hour(tweets)
        return True

    def search_tweets(self, query, tweets):
        """This method takes as argument a query and a list of tweets and
        returns a list with the tweets from the list that contain the query"""
        return [tweet for tweet in tweets if query in tweet]
