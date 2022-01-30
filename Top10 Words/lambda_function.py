from API.GetTweets import get_tweets
from API.CreateTweet import create_tweet

def lambda_handler(x,y):
	def top10_to_tweetable_text(topics):
		new_tweet = ''
		for topic in top10:
			new_tweet += topic + '\n'
	
		return new_tweet



	#get tweets from the API
	top10 = get_tweets()

	#make it pretty
	new_tweet = top10_to_tweetable_text(top10)

	#Tweet the top 10 list
	status = create_tweet(new_tweet)

	#if errors, print status
	if len(status[2]) > 0:
		print(status)
