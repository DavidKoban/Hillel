from django.shortcuts import render
from django.views.generic import TemplateView
from Garden.models import Tree, Fruit


class My_View_Tree(TemplateView):
    template_name = 'tree.html'

    def get_context_data(self, **kwargs):
        return {
            'trees': [
                {
                    'kind': tree.kind,
                    'index': tree.index,
                    'landing_day': tree.landing_day,
                    'height': tree.height,
                    'width': tree.width,
                    'max_weight_fruit_on_tree': tree.max_weight_fruit_on_tree,
                    'amount_of_fruit': Fruit.objects.filter(tree=tree).count()
                }
                for tree in Tree.objects.order_by("index")
            ],
        }


class My_View_Fruit(TemplateView):
    template_name = 'fruit.html'

    def get_context_data(self, **kwargs):
        return {
            'fruits': [
                {
                    'index': fruit.index,
                    'tree': fruit.tree,
                    'weight': fruit.weight,
                }
                for fruit in Fruit.objects.order_by("index")
            ],
        }


class Fruits_of_tree(TemplateView):
    template_name = "fruit_of_tree.html"

    def get_context_data(self, **kwargs):
        index_tree = self.kwargs['index']
        tree = Tree.objects.get(index=index_tree)
        return {
            'index_tree': tree,
            'fruits': [
                {
                    'index': fruit.index,
                    'tree': fruit.tree,
                    'weight': fruit.weight,
                }
                for fruit in Fruit.objects.filter(tree=tree).order_by("index")
            ],
        }

