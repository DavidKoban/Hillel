import uuid
from django.db import models
from App_1.models import Auctioneer


class Slot(models.Model):
    auctioneer = models.ForeignKey('Auctioneer', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=50, default='Slot')
    description = models.CharField(max_length=200, null=True, default='Description')
    start_price = models.FloatField(null=False, default=0)
    end_price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} {self.name}"
