from API.GetTweets import get_most_liked_tweet
from API.CreateTweet import retweet


def lambda_handler(x,y):

	keywords = ["Yaounde", "yaounde", "Yaoundé", "yaoundé"]

	#get tweets from the API
	liked_tweet_id = get_most_liked_tweet(keywords)

	if liked_tweet_id != 0: 
		#Tweet the top 10 list
		status = retweet(liked_tweet_id)

		#if errors, print status
		if len(status[2]) > 0:
			print(status)
