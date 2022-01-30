#Create a tweet

import tweepy
from API.APIKeys import Key, Secret, Access_Token, Access_Secret, Bearer_Token

def auth():
	client = tweepy.Client(bearer_token=Bearer_Token,
                       consumer_key=Key,
                       consumer_secret=Secret,
                       access_token=Access_Token,
                       access_token_secret=Access_Secret)
	return client

def create_tweet(tweet_text):
	# Replace the text with whatever you want to Tweet about
	client = auth()

	tweet_text = "Paul Biya est à la une:\n\n" + tweet_text
	response = client.create_tweet(text=tweet_text)

	return response
	
def retweet(tweet_id):
	client = auth()
	response = client.retweet(tweet_id)
	return response
	
