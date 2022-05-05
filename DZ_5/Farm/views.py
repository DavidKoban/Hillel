from Garden.models import Tree, Fruit
from rest_framework import generics
from django.views.generic import ListView
from itertools import chain
from operator import attrgetter
from Garden.serializers import FruitSerializer, TreeSerializer


class TreeResponseView(generics.ListAPIView):
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()


class FruitResponseView(generics.ListAPIView):
    serializer_class = FruitSerializer
    queryset = Fruit.objects.select_related('tree').all()


class FruitListView(ListView):
    template_name = 'fruit.html'
    paginate_by = 3
    page_kwarg = 'stranitsa'

    def get_queryset(self):
        fruit_list = Fruit.objects.all()

        result_list = sorted(
            chain(fruit_list),
            key=attrgetter('index'),
            )

        return result_list

