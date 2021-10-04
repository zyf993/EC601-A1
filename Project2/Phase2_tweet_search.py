import os
import tweepy #Use tweepy library
import pandas as pd

#input your keys here
consumer_key = ""
consumer_secret = ""
access_key  = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit =True)

def search_tweets():
    search_words = "Boston"
    date_since = "2021.9.1"
    show_newest_num = 5#input news numbers
    tweets = tweepy.Cursor(api.search_tweets, q=search_words,lang="en",since_id=date_since).items(10)

    # Iterate and print tweets
    list = []
    for tweet in tweets:
        tweet = tweet.text
        list.append(tweet)
    return list



if __name__ == '__main__':
    # print(twitter_content())
    # print(My_Home_tweets())
    # print(search_user_infor())
    # print(search_tweets())

    f=open("tweets.txt","w",encoding='utf-8')
     
    for line in search_tweets():
        f.write(line+'\n')
    f.close()