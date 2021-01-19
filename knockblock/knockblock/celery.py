from __future__ import absolute_import

import os
from django.conf import settings
from celery import Celery
import json

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knockblock.settings')

from django.conf import settings  # noqa

# ,broker='amqp://localhost')#http://localhost:15672')#amqp://guest@localhost//'))
app = Celery('knockblock')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    # CELERY_RESULT_BACKEND = 'cache',
    # CELERY_CACHE_BACKEND = 'memory'
    #CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'
    #CELERY_RESULT_BACKEND = 'rpc://'

    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# @app.task(bind=True)
# def twitter_job(twitt_input):
# 	inputdict = {"inputt": twitt_input}
# 	print inputdict
# 	#sys.argv = [settings.STATIC_BREV + static('last24h/tweet.py'), inputt]
# 	execfile(settings.STATIC_ROOT + 'tweet.py',inputdict)
