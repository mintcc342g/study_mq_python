from .models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        event = Event.objects.all()
        model = Event
        fields = '__all__'

class PayloadSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(help_text="user_id")
    message = serializers.CharField(help_text="user's message")

class EventBodySerializer(serializers.Serializer):
    payload = PayloadSerializer()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        message = Message.objects.all()
        model = Message
        fields = '__all__'
