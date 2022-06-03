from rest_framework import generics, exceptions
from Sloter.models.Bet import Bet
from Sloter.models.Slot import Slot
from Sloter.serializers.BetSerializer import BetSerializer
from django.utils.functional import cached_property
from django.utils import timezone
from django.db import transaction


class BetView(generics.ListCreateAPIView):
    serializer_class = BetSerializer

    @cached_property
    def slot(self):
        slots = Slot.objects.filter(has_ended=False)  #  1.last_price = 100 2. last_price = 100
        return generics.get_object_or_404(slots, **self.kwargs)

    def get_queryset(self):
        return Bet.objects.filter(user=self.request.user, slot=self.slot)

    @transaction.atomic
    def perform_create(self, serializer):
        bet = serializer.save()
        bet.slot.add_bet(bet)
