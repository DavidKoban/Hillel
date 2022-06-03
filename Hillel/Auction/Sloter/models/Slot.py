from .BasicModel import BasicModel
from django.db import models
from django.conf import settings
from rest_framework import exceptions
from decimal import Decimal


class Slot(BasicModel):
    auctioneer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_slots')
    description = models.CharField(max_length=200, null=True, default='Description')
    start_price = models.FloatField(null=False, default=0)
    current_price = models.FloatField(null=True)
    end_price = models.FloatField(null=True)
    end_time = models.DateTimeField(null=True, )

    has_ended = models.BooleanField(default=False, )

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name='bought_slots')

    def __str__(self):
        return f"{self.id} {self.name}"

    def add_bet(self, bet):
        # with Lock(f"bet_lock_{self.id}").acquire():
        self.refresh_from_db()
        if (self.current_price or self.start_price) * Decimal(1.05) > bet.price:
            raise exceptions.ValidationError("Your bet is too small")

        self.current_price = bet.price
        self.save(update_fields=['current_price'])

    def finalize(self):
        if self.has_ended is True:
            raise exceptions.ValidationError("This slot has alread been over")

        last_bet = self.bets.first()
        assert last_bet.price == self.end_price
        self.buyer_id = last_bet.user_id
        self.has_ended = True
        self.save(update_fields=['buyer_id', 'has_ended', ])
