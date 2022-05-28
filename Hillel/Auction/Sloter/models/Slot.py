from .BasicModel import BasicModel
from django.db import models
from django.conf import settings


class Slot(BasicModel):
    auctioneer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, default='Description')
    start_price = models.FloatField(null=False, default=0)
    end_price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} {self.name}"
