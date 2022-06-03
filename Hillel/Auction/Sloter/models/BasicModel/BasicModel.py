import uuid
from django.db import models
from django.utils import timezone


class BasicModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=50, default="Ivan")
    created = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-created', )
