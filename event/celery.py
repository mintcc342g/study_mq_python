from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings

app = Celery('event', include=['event.handler'])
app.conf.update(settings.CELERY_EVENT)

if __name__ == '__main__':
    app.start()
