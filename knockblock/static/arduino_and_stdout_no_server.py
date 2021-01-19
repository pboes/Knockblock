# Single script version of the whole setup, in which hastags are written to stdout instead of piped into django.
import serial
import time
# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = 'your token here'
access_token_secret = "'your token_secret here'
consumer_key = 'your API key here'
consumer_secret = 'your secret here'

term = "Knock"

ser = serial.Serial('/dev/tty.usbmodem1411', 19200)

global count

count = 0
class StdOutListener(StreamListener):

    def on_data(self, data):
        #tweet = data['quoted_status']['entities']['hashtags']
        hashtag = []

        # try:
        tweet = json.loads(data)
        hashtags = tweet['entities']['hashtags']
        if len(hashtags) > 0:
            #extract used hastags
            hashtag = tweet['entities']['hashtags'][0]['text']
            #talk to arduino
            ser.write('2')
            time.sleep(0.05)
            ser.write('0')
            print hashtag
        return True

    def on_error(self, status):
        print status

# check serial port
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

#here we specify the terms to track
stream.filter(track=['harm'])
