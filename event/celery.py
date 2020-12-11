from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# 이걸 해줘야 celery worker 가 작동함.
# "프로젝트명.환경설정파일명"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "study_mq_python.settings")

app = Celery('event', include=['event.consumer'])
app.conf.update(settings.CELERY_EVENT)

if __name__ == '__main__':
    app.start()
