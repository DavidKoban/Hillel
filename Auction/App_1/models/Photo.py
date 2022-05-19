import uuid
from django.db import models
from App_1.models import Slot


class Photo(models.Model):
    photo = models.ImageField(upload_to='img', null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slot = models.ForeignKey('Slot', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
