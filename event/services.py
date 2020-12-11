from datetime import timezone, datetime
from api.models import *
from api.serializers import *

# 받은 메세지를 DB에 저장
def send_message(event, payload):
    serializer = MessageSerializer(
        data = {
            "user_id": payload["user_id"],
            "message": payload["message"]
            }
        )
    serializer.is_valid()

    return serializer.save()