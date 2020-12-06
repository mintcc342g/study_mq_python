from datetime import timezone, datetime
from event.service import EventProducer
from .models import *
from .serializers import *

def send_message(event, payload):
    # 이벤트 push
    EventProducer().push_event(event, payload)

    # 이벤트 기록용 db 저장 로직. message queue 랑은 상관없음.
    serializer = EventSerializer(
        data={"name": event, "user_id": payload['user_id']})

    return serializer.save()