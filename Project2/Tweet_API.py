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


#get my twitter tweets
def twitter_content():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        return tweet.text
#get my home tweets
def My_Home_tweets():
    My_Home_tweets = api.home_timeline()
    return My_Home_tweets

#get user information for the user you try to search for
def search_user_infor():
    user_id_search = " "
    screen_name_search =" "
    api.get_user(user_id =user_id_search, screen_name =screen_name_search)

#Search key words and date to show numbers of most recent tweets
#include content, user,hashtag, and http links
def search_tweets():
    search_words = " "
    date_since = " "
    show_newest_num = 5#input news numbers
    tweets = tweepy.Cursor(api.search_tweets, q=search_words,lang="en",since_id=date_since).items(show_newest_num)

    # Iterate and print tweets
    for tweet in tweets:
        return(tweet.text)

    
if __name__ == '__main__':
    print(twitter_content())
    print(My_Home_tweets())
    print(search_tweets())
    print(search_user_infor())



