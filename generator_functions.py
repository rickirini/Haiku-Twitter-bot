import json
from os import listdir
import re
from dpwlibrary import dpwlibrary


def remove_urls(text):
    """This method takes a string as argument and returns string without urls"""
    regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    urls = re.findall(regex, text)
    for url in urls:
        text = text.replace(url[0], ', ')
    return text


def tokenize(string):
    """This method lowercases a string and removes punctuation, returns list of words"""
    stripped = ""
    tweet = []
    for i in string.lower():
        if i.isalnum() or i == '#' or i == '@':
            stripped += i
        else:
            stripped += " "
    nopunct_lower = stripped.split()
    for i in nopunct_lower:
        if i.startswith('#') or i.startswith('@') or i.startswith('rt'):
            continue
        else:
            tweet.append(i)
    return tweet


def extract_tweets(infile):
    """takes file, reads file, returns list of tuples with text of tweet and username"""
    tweets = []
    for line in open(infile, 'r'):
        if 'retweeted_status' in line:
            tweets.append((json.loads(line)['text'], json.loads(line)['retweeted_status']['user']['screen_name']))
        else:
            tweets.append((json.loads(line)['text'], json.loads(line)['user']['screen_name']))
    return tweets


def find_files(directory):
    """ This method takes a directory as argument, we can iterate over directory items (files to be processed),
    returns files list"""
    files = []
    for filename in listdir(directory):
        if filename.endswith(".out"):
            files.append(directory + "/" + filename)
    return files


def accidental_haiku(tweets_dir):
    """This method generates accidental haiku's. Takes directory as argument to function, we can iterate over directory items (files to be processed),
    return suitable list of accidental haiku tweets"""
    dict_lettergrepen = dpwlibrary()
    tokenized = []
    tweets = []

    for file in find_files(tweets_dir):
        for tweet, user in extract_tweets(file):
            aantal_let = 0
            tweet_let = 0
            regel1 = ""
            regel2 = ""
            regel3 = ""
            haikulist = []
            dirtylist = []

            # count lettergrepen + check if all tokens from tweet exist in dictionary
            for word in tokenize(remove_urls(tweet)):
                dirtylist.append(word)  # set all words from tweet in list
                if word in dict_lettergrepen.keys():
                    aantal_let = aantal_let + int(dict_lettergrepen[word])
                    haikulist.append(word)  # set words from tweet conform dictonary in list
                else:
                    break

            # filter lettergrepen (min 17)
            if aantal_let == 17:

                skip = False  # de iteratie 1x wanneer 5 lettergrepen gevonden zijn

                # genereer haiku regels
                for x in haikulist[:]:
                    # regel 1
                    if tweet_let < 6 and skip is False:
                        if int(dict_lettergrepen[x]) < 6:
                            if tweet_let + int(dict_lettergrepen[x]) < 6:
                                tweet_let = tweet_let + int(dict_lettergrepen[x])
                                regel1 = regel1 + x + " "
                                if tweet_let == 5:
                                    skip = True  # change skip status for line 2
                                    continue
                            else:
                                break

                    # regel 2
                    if 5 <= tweet_let <= 13 and skip is True:
                        if int(dict_lettergrepen[x]) < 8:
                            if tweet_let + int(dict_lettergrepen[x]) < 13:
                                tweet_let = tweet_let + int(dict_lettergrepen[x])
                                regel2 = regel2 + x + " "
                                if tweet_let == 12:
                                    skip = False  # change skip status for line 3
                                    continue

                            else:
                                break

                    # regel 3
                    if tweet_let >= 12 and skip is False:
                        if int(dict_lettergrepen[x]) < 6:
                            if tweet_let + int(dict_lettergrepen[x]) < 18:
                                tweet_let = tweet_let + int(dict_lettergrepen[x])
                                regel3 = regel3 + x + " "
                            else:
                                break

                # check haiku regels conform 5 / 7 / 5
                # and check if
                # set check regel 1
                check1 = regel1.split()
                checkcount1 = 0
                for word in check1:
                    checkcount1 = checkcount1 + dict_lettergrepen[word]

                # set check regel 2
                check2 = regel2.split()
                checkcount2 = 0
                for word in check2:
                    checkcount2 = checkcount2 + dict_lettergrepen[word]

                # set check regel 3
                check3 = regel3.split()
                checkcount3 = 0
                for word in check3:
                    checkcount3 = checkcount3 + dict_lettergrepen[word]

                # check regels + check if all words exist in dictionary
                if checkcount1 == 5 and checkcount2 == 7 and checkcount3 == 5 and (len(dirtylist) - len(haikulist) == 0):
                    tweet = "{0}\n{1}\n{2}\n@{3}".format(regel1, regel2, regel3, user)
                    tweets.append(tweet)

    return tweets


def random_haiku(tweets_dir):
    """This method generates random haikus. Takes directory as argument to
    function, we can iterate over directory items (files to be processed),
    returns suitable list of random haiku tweets"""

    dict_lettergrepen = dpwlibrary()
    tokenized = []
    tweets = []

    for file in find_files(tweets_dir):
        for tweet, user in extract_tweets(file):
            aantal_let = 0
            tweet_let = 0
            regel1 = ""
            regel2 = ""
            regel3 = ""
            haikulist = []
            dirtylist = []
            tokenized.append(tokenize(remove_urls(tweet)))

            # count lettergrepen + check if all tokens from tweet exist in dictionary
            for word in tokenize(remove_urls(tweet)):
                dirtylist.append(word)  # set all words from tweet in list
                if word in dict_lettergrepen.keys():
                    aantal_let = aantal_let + int(dict_lettergrepen[word])
                    haikulist.append(word)  # set words from tweet conform dictonary in list
                else:
                    break

            # filter lettergrepen (min 17)
            if aantal_let == 17:

                # regel 1
                for x in haikulist[:]:
                    if x in dict_lettergrepen:
                        if tweet_let < 6:
                            if int(dict_lettergrepen[x]) < 6:
                                if tweet_let + int(dict_lettergrepen[x]) < 6:
                                    tweet_let = tweet_let + int(dict_lettergrepen[x])
                                    regel1 = regel1 + x + " "
                                    haikulist.remove(x)

                # regel 2
                for x in haikulist[:]:
                    if x in dict_lettergrepen:
                        if 5 <= tweet_let <= 13:
                            if int(dict_lettergrepen[x]) < 8:
                                if tweet_let + int(dict_lettergrepen[x]) < 13:
                                    tweet_let = tweet_let + int(dict_lettergrepen[x])
                                    regel2 = regel2 + x + " "
                                    haikulist.remove(x)

                # regel 3
                for x in haikulist[:]:
                    if x in dict_lettergrepen:
                        if tweet_let >= 12:
                            if int(dict_lettergrepen[x]) < 6:
                                if tweet_let + int(dict_lettergrepen[x]) < 18:
                                    tweet_let = tweet_let + int(dict_lettergrepen[x])
                                    regel3 = regel3 + x + " "
                                    haikulist.remove(x)

                # check haiku regels conform 5 / 7 / 5
                check1 = regel1.split()
                checkcount1 = 0
                for word in check1:
                    checkcount1 = checkcount1 + dict_lettergrepen[word]

                check2 = regel2.split()
                checkcount2 = 0
                for word in check2:
                    checkcount2 = checkcount2 + dict_lettergrepen[word]

                check3 = regel3.split()
                checkcount3 = 0
                for word in check3:
                    checkcount3 = checkcount3 + dict_lettergrepen[word]
                if checkcount1 == 5 and checkcount2 == 7 and checkcount3 == 5:
                    tweet = "{0}\n{1}\n{2}\n@{3}".format(regel1, regel2, regel3, user)
                    tweets.append(tweet)

    return tweets
