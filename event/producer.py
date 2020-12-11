from __future__ import absolute_import, unicode_literals

from django.conf import settings

from kombu.pools import producers, reset
from kombu import Exchange, Queue
from kombu import Connection

import logging

logger = logging.getLogger('MQ Study')
task_exchange = Exchange('study.message.queue', type='topic')

# MQ에 message를 보낼 때 사용
class EventProducer():
    _conn = None
    def __init__(self, routing_key='mq.study.event'):
        self._route = routing_key
        self._connection()

    def _connection(self):
        if not EventProducer._conn:
            try:
                EventProducer._conn = Connection(settings.BROKER_URL)
                EventProducer._conn.ensure_connection(max_retries=2)
                logger.info("EvnetProducer connected")
            except Exception as e:
                logger.error(f"Unable to connect to broker[{settings.BROKER_URL}]")
                raise e

    def push_event(self, event, payload):
        event_msg = {'event': event, 'payload': payload}
        logger.info(f'push_event: {event} {payload}')
        with producers[EventProducer._conn].acquire(block=True) as producer:
            publish = EventProducer._conn.ensure(producer, producer.publish, errback=self.errback, max_retries=3)
            publish(event_msg, serializer='pickle', compression='bzip2', exchange=task_exchange, declare=[task_exchange], routing_key=self._route)

    def errback(self, exc, interval):
        logger.error('push_event errback: %r', exc, exc_info=1)
        logger.info(f'push_event retry in {interval} seconds')
        reset()
