from django.db import models


class User(models.Model):
    id = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=50)