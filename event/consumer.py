import logging
from celery import bootsteps
from kombu import Consumer, Exchange, Queue
from event.celery import app
from . import services as consumer_svc
from django.db import connections

logger = logging.getLogger("MQ Study")

task_exchange = Exchange('study.message.queue', type='topic') # 이런 형태의 Exchange를 가진 msg만 받게 될 것
task_queues = [Queue('my_event', task_exchange, routing_key='mq.study.*')]
'''
Topic 이란?
  - 메세지 routing key를 지정하고 그 key를 근거로 Message Queue를 선택함.
  - key 패턴에는 * 또는 # 을 사용할 수 있음. (kombu 공식 문서에서 Topic Exchanges 부분 참고)
'''


# MQ에 쌓인 message를 소비
class EventConsumer(bootsteps.ConsumerStep):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.consumer_svc = consumer_svc

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=task_queues,
                         accept=['pickle', 'json'],
                         callbacks=[self.handle_message])]

    def handle_message(self, body, message):
        try:
            event = body['event']
            payload = body['payload']
            logger.info(f'Got event: {event} {payload}')

            self.event_dispatcher(event, payload)
        except Exception as exc:
            logger.error('task raised exception: %r', exc)
        message.ack()

    def event_dispatcher(self, event, payload):
        self.close_db_connections()
        event_func = getattr(self.consumer_svc, event.replace(".", "_"), self.no_event_func)
        event_func(event, payload)

    def no_event_func(self, payload, event):
        logger.error(f"unknown event [{event}] [{payload['user_id']}]")

    def close_db_connections(self):
        for conn in connections.all():
            conn.close()


app.steps['consumer'].add(EventConsumer)
