# controller.py
"""This module provides a Controller class"""
import time
import threading


class Controller:
    """This class takes the right actions based on the user's choices"""

    def __init__(self, model, view):
        """initializes Controller class with model
            and view classes as arguments"""
        self.model = model
        self.view = view
        self.generatable = False
        self.generatable_random = False
        self.retweet = False
        self.stop = False
        self.breakthread = False
        self.clicked = ""

    def background_retweet(self):
        """This method makes sure that the retweet process can
        take place in the background and you can still use the
        interface to do other things (e.g. display tweets)"""
        while self.breakthread is False:
            try:
                self.model.retweet_hour(self.tweets)  # connects twitter
            except RuntimeError:
                pass

            if self.breakthread is True:
                break

    def run(self):
        """This method displays the GUI and subsequently waits for user
        event and performs the right action for each user event"""
        self.view.show()
        while True:
            action = self.view.get_action()
            if action == 'tweet button clicked':
                try:
                    self.view.remove_tweet()
                except:
                    pass

                if self.generatable is False:
                    self.retweet = True  # You are allowed to retweet
                    self.accidental_tweets = self.model.generate()  # Generates list from accidental tweets
                    self.generatable = True  # Checks if list doesn't generate again
                    self.tweet = self.model.random_tweet(self.accidental_tweets)  # Grabs a random tweet from the generated list
                    self.view.display(self.tweet)  # Puts the tweet on the screen
                    self.breakthread = False
                    self.clicked = "accidental"

                else:  # Displays a new tweet
                    self.tweet = self.model.random_tweet(self.accidental_tweets)  # Grabs a random tweet from the generated list
                    self.view.display(self.tweet)  # Puts the tweet on the screen
                    self.breakthread = False

            elif action == 'retweet button is clicked':
                if self.retweet:  # Checks if the list is generated
                    self.retweet = self.model.retweet(self.tweet)  # Retweet the random tweet
                    self.breakthread = False
                else:
                    self.view.display("You can only retweet after you've generated a tweet.")

            elif action == 'retweet per hour button is clicked':
                if self.stop is False:
                    if self.clicked == "random":
                        self.tweets = self.model.generate_random()
                    else:
                        self.tweets = self.model.generate()

                    self.retweet = True
                    self.view.remove_per_hour_button()
                    self.view.per_hour_stop_button()
                    self.stop = True
                    self.breakthread = False
                    t = threading.Thread(target=self.background_retweet)
                    t.start()

            elif action == 'per hour stop is clicked':
                self.breakthread = True
                self.view.remove_per_hour_stop_button()
                self.view.per_hour_button()
                self.stop = False

            elif action == 'random tweet button clicked':
                try:
                    self.view.remove_tweet()
                except:
                    pass

                if self.generatable_random is False:
                    self.retweet = True  # You are allowed to retweet
                    self.random_tweets = self.model.generate_random()  # Generates list from random tweets
                    self.generatable_random = True  # Checks if list doesn't generate again
                    self.tweet = self.model.random_tweet(self.random_tweets)  # Grabs a random tweet from the generated list
                    self.view.display(self.tweet)  # Puts the tweet on the screen
                    self.breakthread = False
                    self.clicked = "random"
                    self.side = 2

                else:  # Displays a new tweet
                    self.view.remove_tweet()  # Remove the old tweet
                    self.tweet = self.model.random_tweet(self.random_tweets)  # Grabs a random tweet from the generated list
                    self.view.display(self.tweet)  # Puts the tweet on the screen
                    self.breakthread = False

            elif action == "regular search button clicked":
                self.query = self.view.get_text()
                try:
                    self.view.remove_tweet()
                except:
                    pass
                if self.generatable:
                    self.view.remove_tweet()
                    self.results = self.model.search_tweets(self.query, self.accidental_tweets)
                    if self.results:
                        self.tweet = self.model.random_tweet(self.results)
                        self.view.display(self.tweet)
                    else:
                        self.tweet = "Sorry, no tweets with that query were found."
                        self.view.display(self.tweet)
                else:
                    self.accidental_tweets = self.model.generate()
                    self.results = self.model.search_tweets(self.query, self.accidental_tweets)
                    if self.results:
                        self.tweet = self.model.random_tweet(self.results)
                        self.view.display(self.tweet)
                    else:
                        self.tweet = "Sorry no tweets with that query were found."
                        self.view.display(self.tweet)

            elif action == "random search button clicked":
                self.query = self.view.get_text()
                try:
                    self.view.remove_tweet()
                except:
                    pass
                if self.generatable_random:
                    self.view.remove_tweet()
                    self.results = self.model.search_tweets(self.query, self.random_tweets)
                    if self.results:
                        self.tweet = self.model.random_tweet(self.results)
                        self.view.display(self.tweet)
                    else:
                        self.tweet = "Sorry, no tweets with that query were found."
                        self.view.display(self.tweet)
                else:
                    self.random_tweets = self.model.generate_random()
                    self.results = self.model.search_tweets(self.query, self.random_tweets)
                    if self.results:
                        self.tweet = self.model.random_tweet(self.results)
                        self.view.display(self.tweet)
                    else:
                        self.tweet \
                            = "Sorry, no tweets with that query were found."
                        self.view.display(self.tweet)

            elif action == 'quit button clicked':
                break

        self.view.hide()

if __name__ == '__main__':
    run()
