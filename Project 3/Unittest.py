from google.cloud import language
from Google_analysis import analyze_text_sentiment
import unittest


class TestCaseRun(unittest.TestCase):
	def test_sentiment_score(self):
	    S = analyze_text_sentiment(text)
	    # print(S)
	    if S <= 0:
	        print("Failed, the score is not positive")
	    else:
	        print("Passed, the score is positive")

if __name__ == '__main__':
    f = open("tweets.txt","r",encoding='utf-8')
    text = f.read()  
    f.close()
    #can be import from tweet file
    analyze_text_sentiment(text)
    unittest.main()