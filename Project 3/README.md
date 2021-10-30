# Project 3a
The Unit test here I set one example to test if the sentiment score pass the positive score test. To verify that the twitter that user search get the positive result instead of 0 or negative.
It is important that you import the unittest from python to enable the Unit test function, and also you can import the function from the code you wrote for Twitter.
```
from Google_analysis import analyze_text_sentiment
import unittest
```

Then class the unittest and run it

```
class TestCaseRun(unittest.TestCase):
	def test_sentiment_score(self):
	    S = analyze_text_sentiment(text)
	    # print(S)
	    if S <= 0:
	        print("Failed, the score is not positive")
	    else:
	        print("Passed, the score is positive")
```
The result display as:
Failed, the score is not positive
.
----------------------------------------------------------------------
Ran 1 test in 0.355s

OK

