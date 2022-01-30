from API.GetTweets import get_tweets
from API.CreateTweet import create_tweet, retweet

def lambda_handler(x,y):
	
	def top10_to_tweetable_text(topics):
		new_tweet = ''
		for topic in top10:
			new_tweet += topic + '\n'
	
		return new_tweet
	
	
	
	#get tweets from the API
	top10, count_today, liked_tweet_id = get_tweets()
	
	#only care if today has a lot of tweets
	if count_today > 300:
		#make it pretty
		new_tweet = top10_to_tweetable_text(top10)
	
		#Tweet the top 10 list
		status = create_tweet(new_tweet)
		status = retweet(liked_tweet_id)
	
		#if errors, print status
		if len(status[2]) > 0:
			print(status)
