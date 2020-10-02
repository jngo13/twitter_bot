import json
import tweepy 
import time
import newsapiHeadline
  
# personal details 
consumer_key ="" # Key removed to maintain private access of account
consumer_secret ="" # Key removed to maintain private access of account
access_token ="" # Key removed to maintain private access of account
access_token_secret ="" # Key removed to maintain private access of account
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
  
# time stuff
t = time.localtime()  
current_time = time.strftime("%H%M", t)  

def lambda_handler(event, context):
    # update the status 
    api.update_status(status = newsapiHeadline.makeTweet())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
