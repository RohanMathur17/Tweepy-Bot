import time
import tweepy

consumer_key= "XXX"
consumer_secret  = "XXX"
access_token ="XXX"
access_token_secret= "XXX"
        
    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth , wait_on_rate_limit = True , wait_on_rate_limit_notify = True)

user = api.me()


search = '#postrock'

nrTweets = 50

for tweet in tweepy.Cursor(api.search , search).items(nrTweets):
	try:
		tweet.favorite()
		tweet.retweet()
		time.sleep(20)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break





