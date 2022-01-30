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

num_tweets = 3000

def get_most_liked_tweet(keywords):
	client = tweepy.Client(bearer_token=Bearer_Token)

	# Replace with your own search query
	query = ''
	for x in keywords:
		query += x
		query += ' OR '
		
	query = query[:-3] #drop the last 'OR '
	query += '-is:retweet' #omit retweets
	

	liked_tweet_id = 0
	max_likes = 0
	
	for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at', 'public_metrics', 'entities'], max_results=100).flatten(limit=num_tweets):
		#print(tweet.entities)
		try:
			if len(tweet.entities['urls'][0]['display_url']) > 0:
				if tweet.public_metrics['like_count'] > max_likes:
					max_likes = tweet.public_metrics['like_count']
					liked_tweet_id = tweet.id	
					print(liked_tweet_id)
		except:
			pass

	return liked_tweet_id
