import uuid
from django.db import models


class Auctioneer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, max_length=50, default="Ivan")
    surname = models.CharField(null=True, max_length=50, default="Ivanov")
    patronymic = models.CharField(null=True, max_length=50, default="Ivanovich")

    def __str__(self):
        return f"{self.id} {self.name}"
