import json
import pandas as pd
import matplotlib.pyplot as plt

#tweets data file
file = '/Users/ausubo/karma/insight/project/twitter/t_streams/thrones.txt'

tweets2 = []
for line in open(file):
    try:
        tweet = json.loads(line)
        if 'text' in tweet is not None:
            tweets2.append(tweet)
    except:
        continue

#Create empty dataframe
tweets = pd.DataFrame()

#Select only certain features of tweets to save.
tweets['text'] = map(lambda tweet: tweet.get('text'),tweets2)
tweets['created_at'] = map(lambda tweet:tweet.get('created_at'), tweets2)
tweets['retweeted'] =  map(lambda tweet:tweet.get('retweeted'), tweets2)
tweets['user_followers_count'] = map(lambda tweet:tweet.get('user_followers_count'), tweets2)
tweets['retweet_count'] =  map(lambda tweet:tweet.get('retweet_count'), tweets2)
tweets['favorite_count'] =  map(lambda tweet:tweet.get('favorite_count'), tweets2)
tweets['timestamp'] = pd.to_datetime(tweets['created_at'])


#Deal with text encoding issue.
tweets.to_csv('tweets_thrones.csv', encoding ='utf-8')