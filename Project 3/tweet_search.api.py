import os
import tweepy #Use tweepy library
import pandas as pd

#input your keys here
consumer_key = "ci4obymGas6xANlv2X0wMqeKE"
consumer_secret = "l3oV6bOw47gkOP1z4Pz3bbysilE3Al6Cr4qD0aZdxdymf4CmKa"
access_key  = "1441599120884387841-j55tQ77w1hYJquX8bfJQ6Gn9eUMdxo"
access_secret = "2cBVK4RGp9oUwsYliJC4xY8OsIQaZARr8YEfIVQHq7L6L"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit =True)

def twitter_content():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        return tweet.text

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
