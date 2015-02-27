import tweepy

consumer_key='HZodeLCDcNFh3xlr0LIinU7BW'
consumer_secret='LNPDrDMQAsmkWmH69ryj8dlsxZcT5fwDwvuFsRdBEHpTbb6itz'
access_token='3044509804-LhQhoySGLv92NOZM8xWrUnc6KqjAcyMlQ1tvP9F'
access_token_secret='x2Ls3vycDptwBwaLhLwUEGe2PssQa6cvwiYMkUKOu3is2'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
