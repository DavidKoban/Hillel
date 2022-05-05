from rest_framework import serializers
from Garden.models import Tree, Fruit


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = (
            'kind',
            'index',
            'landing_day',
            'height',
            'width',
            'max_weight_fruit_on_tree',
        )

    def create(self, validated_data):
        return Tree.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.kind = validated_data.get('kind', instance.kind)
        instance.index = validated_data.get('index', instance.index)
        instance.landing_day = validated_data.get('landing_day', instance.landing_day)
        instance.height = validated_data.get('height', instance.height)
        instance.width = validated_data.get('width', instance.width)
        instance.max_weight_fruit_on_tree = validated_data.get('max_weight_fruit_on_tree', instance.max_weight_fruit_on_tree)
        instance.save()
        return instance


class FruitSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Fruit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tree = validated_data.get('tree', instance.tree)
        instance.index = validated_data.get('index', instance.index)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance

    class Meta:
        model = Fruit
        fields = (
            'tree',
            'index',
            'weight',
        )
