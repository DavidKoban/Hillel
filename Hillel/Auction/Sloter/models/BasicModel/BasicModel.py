import uuid
from django.db import models


class BasicModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=50, default="Ivan")

    class Meta:
        abstract = True
