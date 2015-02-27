from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener



consumer_key='HZodeLCDcNFh3xlr0LIinU7BW'
consumer_secret='LNPDrDMQAsmkWmH69ryj8dlsxZcT5fwDwvuFsRdBEHpTbb6itz'
access_token='3044509804-LhQhoySGLv92NOZM8xWrUnc6KqjAcyMlQ1tvP9F'
access_token_secret='x2Ls3vycDptwBwaLhLwUEGe2PssQa6cvwiYMkUKOu3is2'

class listener(StreamListener):
        def on_data(self,data):
            print(data)
            return True
        def on_error(self,status):
            print(status)

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=['@ICC'])
