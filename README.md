# Twitter Cameroon: @atangana_aron
A Twitter bot developed in Python using the Tweepy library and hosted in AWS. 
https://twitter.com/atangana_aron

Cost = Free! 

## The Bot
### Yaounde (Image)
This bot will get a large sample of tweets with the word Yaoundé and then retweet the most liked tweet from the sample with an attached photo. (At present this runs only on Sundays)

### Paul Biya Alert
This bot will run daily and check to see if there is an abnormally large number of relevant Tweets and then retweet the most liked tweet (if there are a lot of Tweets that day). The bot will specifically pull tweets with the word Biya and see how many of them also contain Paul. 

### Top 10 Words
This bot will pull a large sample of tweets with the word Cameroun (French spelling of Cameroon). For each Tweet, it removes stopwords and duplicates, then creates a bag of words counting occurrence of each word. The top 10 words are then tweeted. (At present, this runs every day except Sunday)

## AWS Hosting
### AWS Lambda
Lambda functions have many uses. In this case, we will use it for ultra cheap (free) hosting/computing. All work necessary in AWS to run this bot is done by navigating to Lambda in the AWS UI and creating a new function. The equivalent of main.py for a lambda function is lambda_function.py. To observe the code, start with lambda_function.py and trace its references.

### Non-native Python Packages w/ Lambda
The bot relies on a non-native package (in this case Tweepy). Uploading the code requires also uploading the package. This can be done in several ways, as outlined here: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

### Cloudwatch Events
These are the triggers that will determine when to run your lambda function. Using cron expressions, you can set this on a schedule to run at a certain time per day, day per week/month. 


## Twitter API
### Developer API
https://developer.twitter.com/en/docs/twitter-api
### Tweepy
https://www.tweepy.org/   

A few highlights:
- Max # of tweets pulled at once is 3200
- Can both download tweets and create tweets

## Running this code 
### API Keys
Requires your own APIKeys.py in the API folder. Generate these from the Twitter Developer API. After signing up for a developer account, create a new project and generate read/write keys. Format of APIKeys.py should be as follows:

- Key = 'xxx'
- Secret = 'yyy'
- Bearer_Token = 'zzz'
- Access_Token = '111'
- Access_Secret = '222'

### AWS
Everything in this code runs using the free tiers of AWS. You'll need to create your own account which requires attaching a valid credit card. You'll need to create the lambda function, upload the code as a zip, attach the trigger (Cloudwatch Event), and change the runtime to allow for ~30 seconds or less. 

### Cost
Twitter's API has a limit of number of tweets per month (using the free version). At the time of this writing, that limit is >150x the Tweepy API call limit.  

AWS Lambda has a monthly compute free tier. Each run of a bot is <.1% of that limit at the time of this writing. 
