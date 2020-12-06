from django.shortcuts import render
from datetime import timedelta, timezone, datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.inspectors.base import openapi
from . import services as svc
from .serializers import *

class EventViewSet(viewsets.GenericViewSet):

    serializer_class = EventSerializer

    def __init__(self):
        self.event_svc = svc

    @swagger_auto_schema(request_body=EventBodySerializer)
    def send_events(self, request, event):
        payload = request.data.get('payload', {})
        result = self.event_dispatcher(event, payload)

        return Response(result, status=status.HTTP_201_CREATED)

    def event_dispatcher(self, event, payload):
        event_func = getattr(self.event_svc, event.replace(".", "_"), self.not_exist_func)

        return event_func(event, payload)

    def not_exist_func(self, event, payload):
        err_msg = f"unknown event [{event}], payload [{payload}]"

        return Response(status=status.HTTP_400_BAD_REQUEST)
