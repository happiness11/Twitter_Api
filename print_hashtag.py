
    

import json

results = []

tweets_file = open('tweet_mining.json', "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
 
for tweet in results:
    hashtags = tweet['entities']['hashtags']
    if not hashtags == []:
        print(hashtags)

## down codes is to print individual hashtags without duuplicates




import json



results = []

tweets_file = open('tweet_mining.json', "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
    
new_ht = set()  

# print (tweet["text"])
for tweet in results:
    hashtags = tweet["entities"]["hashtags"]
    # print(hashtags)
    for ht in hashtags:
        new_ht.add(ht["text"])
        print(new_ht)
