from rest_framework import serializers
from Sloter.models.Bet import Bet


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            'id',
            'price',
            'slot',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['slot'] = self.context['view'].slot
        return super(BetSerializer, self).create(validated_data)
