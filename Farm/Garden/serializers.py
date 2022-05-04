from rest_framework import serializers


class TreeSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    kind = serializers.CharField(max_length=200)
    index = serializers.UUIDField(primary_key=True)
    landing_day = serializers.DateField()
    height = serializers.FloatField()
    width = serializers.FloatField()
    max_weight_fruit_on_tree = serializers.FloatField()

