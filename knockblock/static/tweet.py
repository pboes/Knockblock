from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from app1.models import Tweet
from knockblock.celery import app
from celery import current_task
import serial
import time

access_token = 'your token here'
access_token_secret = "'your token_secret here'
consumer_key = 'your API key here'
consumer_secret = 'your secret here'

global inputt, idd

tweets = []


class StdOutListener(StreamListener):

    def on_data(self, data):
        #tweet = data['quoted_status']['entities']['hashtags']
        hashtag = ''
        text = ''
        try:
            tweet = json.loads(data)
            hashtag = '#' + tweet['entities']['hashtags'][0]['text']
            try:
                text = tweet['text'].split(":")[1].split("https")[0]
            except:
                text = tweet['text'].split(":")[1]
        except:
            text = tweet['text']
        try:
            text = text.split("https")[0]
        except:
            None
        print text
        if text not in tweets:
            db = Tweet.objects.get(pk=1)
            db.hashtag = hashtag
            db.tweet = text
            db.save()
            print hashtag
            # ser.write('2')
            time.sleep(0.1)
            # ser.write('0')
        tweets.append(text)
        return True

    def on_error(self, status):
        print status


def checkokay():
    ser.flushInput()
    time.sleep(3)
    line = ser.readline()
    time.sleep(3)

    if line == ' ':
        line = ser.readline()
    print 'here'


# This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

stream.filter(track=[inputt])
