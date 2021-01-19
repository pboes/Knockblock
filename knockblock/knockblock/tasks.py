from __future__ import absolute_import
#from django.conf import settings
from celery import shared_task
import json

@shared_task(name="twitter_job")
def twitter_job(twitt_input):
	idd = twitter_job.request.id
	inputdict = {"inputt": twitt_input,"idd" : idd}
	print inputdict
	#sys.argv = [settings.STATIC_BREV + static('last24h/tweet.py'), inputt]
	execfile('static/tweet.py',inputdict)