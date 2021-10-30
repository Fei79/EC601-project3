import unittest
from Project2 import search_tweets, authentication, sentiment
from Project2 import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy

class TestCaseRun(unittest.TestCase):
    #Test output
    def test_output(self):
        keyword=input()
        output=search_tweets(keyword,1)
        if keyword in output:
            print("Passed")
        else:
            print("Failed")

    #Test search function
    def test_search(self):
        keyword=input()
        api = authentication(consumer_key, consumer_secret, access_token, access_token_secret)
        search_result = tweepy.Cursor(api.search_30_day,
                                      label='project', query=keyword).items(10)          #The correct environment in twitter API
        search_result_new = tweepy.Cursor(api.search_30_day,
                                      label='search', query=keyword).items(10)           #Change label to test search function
        if search_result == search_result_new:
            print("Passed")
        else:
            print("Failed")
            
    #Test sentiment function
    def test_sentiment_score(self):
        sen = sentiment("This year is harder than before")
        if sen.score < 0:
            print("Passed")
        else:
            print("Failed")

if __name__ == '__main__':
    unittest.main()
