# Project 2
Reference : Tweepy link "https://docs.tweepy.org/en/latest/#" use the library and most model here. GoogleNLP model can be checked at the offical website. If using python: "https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3"
# Phase 1
Twitter delayed the developer account application. Notified at the beginning.

Twitter:
Make sure to use the command install tweepy, after choosing the command, find function names in this given verison library.

For example, some verisions have function name as "search_id" insead of "search"
```
pip install tweepy
```
Then from your Twitter developer account, download your keys. Use the following code to connect to your account
```
import tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```
After all settings, apple model and edit code to test the features of twitter api.

GoogleNLP:
To set the googleNLP, we need to have the google cloud account open and create a project. 

Under the project, create a key and download it. Make sure enable API for this project.

If you choose key as a json file, apply CREDENTIALS for google by
```
set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH
```
using cmd, or PowerShell
```
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Every time open a new cmd, you need to redo the above code, or you can write it in code to avoid reset.

Also you need to download the Google Cloud SDK Shell to link to your cloud. After the setting, you can apply the code.
# Phase 2
For my use case, I plan to let users to find the most recent news or information that related with their search key words. And the Google NLP can analysis and give a semtiment score and magnitude towards these tweets's  information. For example, someone tries to find out what's going on in Boston this week.

You can read and write the results from tweet file and import in google NLP to get the analysis result by
```
f=open("tweets.txt","w",encoding='utf-8')
     
for line in search_tweets():
    f.write(line+'\n')
f.close()
```
What I do here is to type key words "Boston" and most recent 10 tweets from September.
In googlenlp file I find the result as

![alt text](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox/QgrcJHrnxSwHMXdcjKSKlMfsfZJDXWLsfqG?projector=1&messagePartId=0.1)

Score: 0.0%

Magnitude: 310.00%



