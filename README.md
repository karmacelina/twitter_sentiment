# twitter_sentiment

TextBlob is used to categorize tweet sentiment polarity.

* json_to_csv.py: turns json file of tweets and puts some of the tweets' data into a csv; outputs tweets_thrones.csv file 
* sentiment.py: analyzes the sentiment of tweets; uses seaborn to create scatter/histogram plot of data; input: tweets_thrones.csv; output: tweets_thrones2.csv file; necessary to deal with unicode issues.
* tweets_time_series.py (work in progress): plots tweet polarity and subjectivity vs time by binning data over a set time interval; splits tweets based on pos, neg, neutral sentiment polarity; input: tweets_thrones2.csv file. 
* word_frequencies.py (work in progress): playing around with nltk to obtain simple word frequency count; input: tweets_thrones2.csv file 

Note: json_to_csv file, sentiment code must be run before tweets_time_series and word_frequencies code.  
