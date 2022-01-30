### Ping Twitter API for Cameroonian Tweets (French only)###
### API developer creds are kept in a separate file ########

from API.APIKeys import Bearer_Token
import tweepy
import re
from collections import defaultdict
#from nltk.corpus import stopwords
from API.stopwords import stopwords_french, stopwords_english
from datetime import date
from datetime import datetime

num_tweets = 2000

def get_stopwords():
	les_stopwords = stopwords_french + stopwords_english
	extra_stopwords = ['paul', 'biya', 'cameroun', '', 'https', 'co', 'ça', 'va', 'cameroon', 'comme', 'si', 'plus', 'ici', 'cette', 'fait', 'quand', 'après', 'orange_cameroun']
	les_stopwords = les_stopwords + extra_stopwords
	return les_stopwords


def get_word_counts_from_API(les_stopwords):
	counter_dict = defaultdict(int)

	client = tweepy.Client(bearer_token=Bearer_Token)

	# Replace with your own search query
	query = 'Biya -is:retweet'

	counter = 0
	
	today = date.today()
	print("Today's date:", today)

	for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at', 'public_metrics'], max_results=100).flatten(limit=num_tweets):
		text = tweet.text
		#convert text to lowercase, no punctuation
		text = text.lower()
		text = re.sub('[^A-Za-z0-9_À-ÿ]+', ' ', str(text))
		words = text.split(' ')

		#remove dupes
		words = list(set(words))

		#print(tweet.created_at)
		#d1 = today
		#d2 = tweet.created_at.date()
		#print(abs((d2 - d1).days))
		

		tweet_day = tweet.created_at.date()
		max_likes = 0
		liked_tweet_id = 0

		#only get Biya tweets related to Paul Biya		
		if abs((tweet_day - today).days) == 0 and 'paul' in words:
			
			#remove stop words and add +1 to word counter for each word
			for word in words:
				if word not in les_stopwords:
					counter_dict[word] += 1
					
			#record most liked tweet
			if tweet.public_metrics['like_count'] > max_likes:
				max_likes = tweet.public_metrics['like_count']
				liked_tweet_id = tweet.id				

			counter += 1

	print(counter, 'tweets read\n')
	return counter_dict, counter, liked_tweet_id



def top_10_topics(counter_dict, counter):
	#output the top 10 list
	top10 = []

	i = 0
	while i < 10:
		top_topic = (max(counter_dict, key = counter_dict.get), counter_dict.pop(max(counter_dict, key = counter_dict.get)))

		#for pretty printing, space if single digit %
		spacer = ''
		if int(top_topic[1]*100/counter) < 10:
			spacer = ' '

		line = str(int(top_topic[1]*100/counter)) + '%' + spacer + ' ' + top_topic[0]
		top10.append(line)

		i += 1

	return top10

def get_tweets():
	les_stopwords = get_stopwords()
	words_dict, num_tweets, most_liked_tweet = get_word_counts_from_API(les_stopwords)
	top10 = top_10_topics(words_dict, num_tweets)
	return top10, num_tweets, most_liked_tweet
