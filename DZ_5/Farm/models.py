from django.db import models
from django.utils import timezone


class Tree(models.Model):
    kind = models.CharField(max_length=200, null=True, default="Some String")
    index = models.AutoField(primary_key=True)
    landing_day = models.DateField(null=True, default=timezone.now)
    height = models.FloatField(null=True, default=0)
    width = models.FloatField(null=True, default=0)
    max_weight_fruit_on_tree = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"{self.kind} {self.index}"


class Fruit(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, null=True, default="Some String")
    index = models.AutoField(primary_key=True)
    weight = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"{self.tree} {self.index}"


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name