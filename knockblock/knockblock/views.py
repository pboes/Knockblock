from app1.models import Tweet
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.conf import settings
from knockblock.tasks import twitter_job
#from celery import current_task
import json
from knockblock.celery import app

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
def twitter(request):
	string = "\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f\x87\xba\xf0\x9f\x87\xb8"
	context = {'initial':string}
	return render(request, 'twitter.html',context) #-{'topic': topic})



def twitter_start(request):
	if request.method == 'POST':
		data = 'Fail'
	#job = customsearch.delay()
		inputt = request.POST.get('input')
		
		job = twitter_job.delay(inputt)
		data = '{"job":"' + str(job.id)+ '"}'    
		json_data = json.dumps(data)
		return HttpResponse(json_data,content_type="application/json")
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

def twitter_update(request):
	data = ''
	if request.method == 'GET':
		tweet = Tweet.objects.get(pk=1)
		data = tweet.tweet + '<br/>' + tweet.hashtag
		#data = data.replace("\n", "<br/>")
		# if 'task_id' in request.GET:
		# 	tweet_job = app.AsyncResult('task_id')
		# 	data = str(tweet_job.result['current'])
	return HttpResponse(data)

def twitter_stop(request):
	if request.method == 'POST':
		result = app.AsyncResult(request.POST.get('id'))
		result.revoke(terminate=True)
		data = 'done'    
		json_data = json.dumps(data)
		return HttpResponse(json_data,content_type="application/json")
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)