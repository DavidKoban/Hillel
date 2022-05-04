from Garden.models import Tree, Fruit, Contact

from rest_framework import generics
from Garden.serializers import FruitSerializer, TreeSerializer



class TreeResponseView(generics.ListAPIView):
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()


class FruitResponseView(generics.ListAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.select_related('tree').all()

