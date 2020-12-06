from django.urls import path
from django.conf import settings

from .views import *

urlpatterns = [
    path("event/<str:event>", EventViewSet.as_view({'post': 'send_events'}), name="send_events"),
]
