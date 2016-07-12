#Analysis of twitter sentiment using TextBlob

#Define sentiment and subjectivity function to be applied on tweets' text.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from textblob import TextBlob

def sentiment(text):
    '''Compute sentiment from utf8 string, returns polarity'''
    return TextBlob(str(text).decode('utf8')).sentiment[0]

def subjectivity(text):
    '''Compute sentiment from utf8 string, returns subjectivity'''
    return TextBlob(str(text).decode('utf8')).sentiment[1]

#Import csv file with correctly encoded text (output from json_to_csv.py file)
tweets = pd.read_csv('tweets_thrones.csv')


#Add two new columns with sentiment info to tweets dataframe
tweets['polarity'] = tweets['text'].apply(sentiment) # Analyse
tweets['subjectivity'] = tweets['text'].apply(subjectivity)

#Output dataframe into csv; deals with utf-8 encoding issue
tweets.to_csv('tweets_thrones2.csv', encoding ='utf-8')

sns.jointplot(x="subjectivity", y="polarity", data=tweets);
plt.savefig('thrones_subj_pol_scatter_hist.png', dpi=300)