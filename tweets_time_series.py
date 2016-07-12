import pandas as pd
import matplotlib.pyplot as plt

#Import tweets
tweets = pd.read_csv('tweets_thrones2.csv')

#Create smaller data frame
df_bin =pd.DataFrame()
df_bin['time'] = pd.to_datetime(tweets['timestamp'])
df_bin['polarity'] = tweets['polarity']
df_bin['subjectivity'] = tweets['subjectivity']


import seaborn as sns
#create plots of polarity and subjectivity vs time binned every # minutes
df_bin.set_index('time').resample('5min').mean().plot()
plt.savefig('thrones_subj_pol_timeseries.png', dpi=300)

#eliminate tweets with "RT" string
#check how to eliminate via <<< future work!
df_noRT = tweets[tweets['text'].str.contains("RT")==False]


df_noRT_pos = df_noRT[df_noRT['polarity']>0]
df_noRT_neg = df_noRT[df_noRT['polarity']<0]
df_noRT_neutral = df_noRT[df_noRT['polarity']==0]


