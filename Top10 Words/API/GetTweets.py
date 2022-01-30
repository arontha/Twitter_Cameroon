### Ping Twitter API for Cameroonian Tweets (French only)###
### API developer creds are kept in a separate file ########

from API.APIKeys import Bearer_Token
import tweepy
import re
from collections import defaultdict
#from nltk.corpus import stopwords
from API.stopwords import stopwords_french, stopwords_english

num_tweets = 2000

def get_stopwords():
	les_stopwords = stopwords_french + stopwords_english
	extra_stopwords = ['cameroun', '', 'https', 'co', 'ça', 'va', 'cameroon', 'comme', 'si', 'plus', 'ici', 'cette', 'fait', 'quand', 'après', 'orange_cameroun']
	les_stopwords = les_stopwords + extra_stopwords
	return les_stopwords


def get_word_counts_from_API(les_stopwords):
	counter_dict = defaultdict(int)

	client = tweepy.Client(bearer_token=Bearer_Token)

	# Replace with your own search query
	query = 'cameroun Cameroun -is:retweet'

	counter = 0

	for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=num_tweets):
		#convert text to lowercase, no punctuation
		text = tweet.text
		text = text.lower()
		text = re.sub('[^A-Za-z0-9_À-ÿ]+', ' ', str(text))
		words = text.split(' ')
    
		#remove dupes
		words = list(set(words))

		#remove stop words and add +1 to default dict
		for word in words:
			if word not in les_stopwords:
				counter_dict[word] += 1  		    
    
		counter += 1
        
	print(counter, 'tweets read\n')
	return counter_dict, counter



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
	words_dict, num_tweets = get_word_counts_from_API(les_stopwords)
	top10 = top_10_topics(words_dict, num_tweets)
	return top10
