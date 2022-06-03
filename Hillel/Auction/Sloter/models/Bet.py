from .BasicModel import BasicModel
from django.db import models
from django.conf import settings
from Sloter.models.Slot import Slot


class Bet(BasicModel):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.user.email} - {self.price} - {self.slot}"
