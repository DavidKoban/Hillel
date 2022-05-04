from django.db import models
from django.utils import timezone


class Tree(models.Model):
    kind = models.CharField(max_length=200)
    index = models.AutoField(primary_key=True)
    landing_day = models.DateField()
    height = models.FloatField()
    width = models.FloatField()
    max_weight_fruit_on_tree = models.FloatField()

    def __str__(self):
        return f"{self.kind} {self.index}"


class Fruit(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, null=True)
    index = models.AutoField(primary_key=True)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.tree} {self.index}"
