import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '54LxUVaH0m60f6jksl8KRjL0x'
CONSUMER_SECRET = 'NMlzQwz0IUKNb2BMtMLAIVAlDlwCRr2KosZQ7sE9jXmoPR5WhE'
OAUTH_TOKEN = '756425691386748928-vnV7zu9bvbpxFf7jcNTNZK7WW3NGc9G'
OAUTH_TOKEN_SECRET = 'hl4EUIXlmtmklH6sBDhgcCnThK9MiOvlV5dxCOi14sezj'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)
         
DUB_WOE_ID = 560743
LON_WOE_ID = 44418
 
 
dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
 
dub_trends_set = set([trend['name']
                   for trend in dub_trends[0]['trends']])
 
lon_trends_set = set([trend['name']
                  for trend in lon_trends[0]['trends']])
 
common_trends = set.intersection(dub_trends_set, lon_trends_set)
 
 
print (common_trends)
