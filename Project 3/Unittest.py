from google.cloud import language
from Google_analysis import analyze_text_sentiment
from tweet_search_api import twitter_content
import unittest 

class TestStringMethods(unittest.TestCase):
	def test_sentiment_score(self):
	    S = analyze_text_sentiment(text)
	    # assert S >= 0
	    msg = 'score is smaller than zero'
	    self.assertTrue(S >= 0, msg)

	def test_negative(self):
	    # error message in case if test case got failed 
	    message = "Test value is none"
	    # assertIsNotNone() to check that if input value is not none 
	    self.assertIsNotNone(twitter_content, message) 

if __name__ == '__main__':
    f = open("tweets.txt","r",encoding='utf-8')
    text = f.read()  
    f.close()
    #can be import from tweet file
    analyze_text_sentiment(text)
    #call the unit test function
    unittest.main()