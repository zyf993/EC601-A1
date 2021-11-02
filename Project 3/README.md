# Project 3a
The Unit test here I set one example to test if the sentiment score pass the positive score test. To verify that the twitter that user search get the positive result instead of 0 or negative.
It is important that you import the unittest from python to enable the Unit test function, and also you can import the function from the code you wrote for Twitter.
```
from Google_analysis import analyze_text_sentiment
import unittest
```

Then class the unittest and run it

```
class TestStringMethods(unittest.TestCase):
	def test_sentiment_score(self):
	    S = analyze_text_sentiment(text)
	    msg = 'score is smaller than zero'
	    self.assertTrue(S >= 0, msg)
```

Also test if the api can get messages instead of None from twitter by using the following code.
```
self.assertIsNotNone(twitter_content, message)
```

The result display as:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.274s

OK
```
