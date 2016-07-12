# twitter_sentiment

TextBlob is used to categorize tweet sentiment polarity.

* json_to_csv.py: turns json file of tweets and puts some of the tweets' data into a csv 
* sentiment.py: analyzes the sentiment of tweets; uses seaborn to create scatter/histogram plot of data
* tweets_time_series.py (work in progress): plots tweet polarity and subjectivity vs time by binning data over a set time interval; splits tweets based on pos, neg, neutral sentiment polarity 
* word_frequencies.py (work in progress): playing around with nltk to obtain simple word frequency count. 

Note: json_to_csv file, sentiment code must be run before tweets_time_series and word_frequencies code.  
