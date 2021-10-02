# Project 2
Reference : Tweepy link "https://docs.tweepy.org/en/latest/#" use the library and most model here.
# Phase 1
Twitter delayed the developer account application. Notified at the beginning.
Make sure to use the command install tweepy, after choosing the command, find function names in this given verison library. For example, some verisions have function name as "search_id" insead of "search"
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