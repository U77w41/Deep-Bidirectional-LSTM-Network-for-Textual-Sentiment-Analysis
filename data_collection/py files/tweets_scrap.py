import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import os
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

consumerKey = '3raNDxoSu2ET9kMpCBspET9vY'
consumerSecret = 'LCsFcsS6iXxpxGKP8Ye5h5TZv0wOXKTSnfPBhpQblRycjThmag'
accessToken = '394502765-d1Nh5LM38bL3d7zHSxUKy9jQkgXruK09yIUIKkZA'
accessTokenSecret = '0sGbEhACcf19i5c0MkZLizOdaU1jxFRDDrk0Qmn09EgeA'

authenticate = tweepy.OAuthHandler(consumerKey,consumerSecret)
authenticate.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(authenticate, wait_on_rate_limit= True)

search_term = "#cryptocurrency -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets, 
                       q=search_term , 
                       lang = 'en',
                       since = '2021-09-01',
                       tweet_mode = 'extended').items(5000)


all_tweets = [tweet.full_text for tweet in tweets]

all_tweets