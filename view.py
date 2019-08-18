# view.py
"""This module provides a class for creating a GUI"""
from graphics import *
from graphics_util import is_within


class GUIView:
    """This class models a GUI"""

    def show(self):
        """This method draws all constant objects in the GUI"""
        self.win = GraphWin('Tweeku', 800, 500)
        self.welcome = Text(Point(400, 75), 'Welcome to the Tweeku Generator')
        self.welcome.draw(self.win)
        self.welcome.setFace('arial')
        self.welcome.setSize(17)

        self.generate_tweet = Rectangle(Point(200, 300), Point(390, 260))
        self.generate_tweet.draw(self.win)
        self.generate_tweet.setFill(color_rgb(51, 204, 255))

        self.generator_text = Text(Point(295, 280), 'Generate Tweeku')
        self.generator_text.draw(self.win)
        self.generator_text.setStyle('bold')
        self.generator_text.setSize(14)
        self.generator_text.setFace('arial')

        self.generate_tweet_random = Rectangle(Point(410, 300), Point(600, 260))
        self.generate_tweet_random.draw(self.win)
        self.generate_tweet_random.setFill(color_rgb(51, 204, 255))
        self.generator_text_random = Text(Point(505, 280), 'Generate Random Tweeku')
        self.generator_text_random.draw(self.win)
        self.generator_text_random.setStyle('bold')
        self.generator_text_random.setSize(11)
        self.generator_text_random.setFace('arial')

        self.retweet = Rectangle(Point(440, 360), Point(500, 420))
        self.retweet_picture = Image(Point(470, 390), 'retweet.gif')
        self.retweet_picture.draw(self.win)
        self.retweet.draw(self.win)

        self.retweet_hour = Rectangle(Point(360, 360), Point(420, 420))
        self.retweet_hour_picture = Image(Point(390, 390), 'clock.gif')
        self.retweet_hour_picture.draw(self.win)
        self.retweet_hour.draw(self.win)

        self.retweet_hour_stop = Rectangle(Point(270, 360), Point(330, 420))
        self.retweet_hour_picture_stop = Image(Point(300, 390), 'stop.gif')
        self.retweet_hour_stop_text = Text(Point(390, 390), 'Tweet per hour \n is active')
        self.retweet_hour_stop_text.setSize(11)

        self.search = Entry(Point(330, 465), 20)
        self.search.draw(self.win)
        self.search_reg_button = Rectangle(Point(430, 450), Point(480, 480))
        self.search_reg_button.draw(self.win)
        self.search_reg_text = Text(Point(455, 465), "Reg. Search")
        self.search_reg_text.setSize(6)
        self.search_reg_text.draw(self.win)
        self.search_random_button = Rectangle(Point(490, 450), Point(540, 480))
        self.search_random_button.draw(self.win)
        self.search_random_text = Text(Point(515, 465), "Rand. Search")
        self.search_random_text.draw(self.win)
        self.search_random_text.setSize(6)

        self.quit_button = Rectangle(Point(760, 10), Point(790, 40))
        self.quit_button.draw(self.win)
        self.quit_button.setFill(color_rgb(51, 204, 255))
        self.quit_text = Text(Point(775, 25), 'X')
        self.quit_text.draw(self.win)
        self.quit_text.setSize(22)
        self.quit_text.setStyle('bold')
        pass

    def get_action(self):
        """This method waits for a user action and responds appropriately, returns string"""
        try:
            mouse = self.win.getMouse()
            if is_within(mouse, self.generate_tweet):
                return 'tweet button clicked'

            elif is_within(mouse, self.retweet_hour):
                return 'retweet per hour button is clicked'

            elif is_within(mouse, self.retweet):
                return 'retweet button is clicked'

            elif is_within(mouse, self.retweet_hour_stop):
                return 'per hour stop is clicked'

            elif is_within(mouse, self.quit_button):
                return 'quit button clicked'

            elif is_within(mouse, self.generate_tweet_random):
                return 'random tweet button clicked'

            elif is_within(mouse, self.search_reg_button):
                return "regular search button clicked"

            elif is_within(mouse, self.search_random_button):
                return "random search button clicked"

        except GraphicsError:
            return 'quit'

    def display(self, tweet):
        """This method draws a tweeku in the GUI, takes as argument the tweeku to be drawn"""
        self.tweet_text = Text(Point(400, 175), tweet)
        self.tweet_text.draw(self.win)

    def remove_tweet(self):
        """This method removes an existing tweeku from the GUI"""
        self.tweet_text.undraw()

    def remove_per_hour_button(self):
        """This method removes the tweet per hour button"""
        self.retweet_hour_picture.undraw()
        self.retweet_hour.undraw()

    def per_hour_stop_button(self):
        """This method draws the per hour stop button"""
        self.retweet_hour_stop.draw(self.win)
        self.retweet_hour_picture_stop.draw(self.win)
        self.retweet_hour_stop_text.draw(self.win)

    def per_hour_button(self):
        """This method draws the per hour button"""
        self.retweet_hour_picture.draw(self.win)
        self.retweet_hour.draw(self.win)

    def remove_per_hour_stop_button(self):
        """This method removes the per hour stop button"""
        self.retweet_hour_stop.undraw()
        self.retweet_hour_picture_stop.undraw()
        self.retweet_hour_stop_text.undraw()

    def get_text(self):
        """This method returns the text currently in the text entry, returns string"""
        return self.search.getText()

    def hide(self):
        """This method hides the GUI window"""
        self.win.close()
        pass
