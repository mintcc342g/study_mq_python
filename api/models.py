from django.db import models

class Event(models.Model):

    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_id = models.BigIntegerField(null=False)
    name = models.CharField(null=False, max_length=128)

    class Meta:
        managed = True
        db_table = "events"
        app_label = "event"
