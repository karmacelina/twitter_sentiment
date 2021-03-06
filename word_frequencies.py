import matplotlib
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist

tweets = pd.read_csv('tweets_thrones2.csv')
df_noRT = tweets[tweets['text'].str.contains("RT")==False]

stop = stopwords.words('english')
text = df_noRT['text']

tokens = []
for txt in text.values:
    tokens.extend([t.lower().strip(":,.") for t in txt.split()])

filtered_tokens = [w for w in tokens if not w in stop]

freq_dist = nltk.FreqDist(filtered_tokens)
freq_dist.plot(15)
