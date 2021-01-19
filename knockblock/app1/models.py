from django.db import models

class Tweet(models.Model):
    tweet = models.CharField(max_length=400)
    hashtag = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.tweet