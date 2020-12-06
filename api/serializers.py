from .models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        event = Event.objects.all()
        model = Event
        fields = '__all__'

class PayloadSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(help_text="user_id(pk)")

class EventBodySerializer(serializers.Serializer):
    payload = PayloadSerializer()
