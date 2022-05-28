from .BasicModel import BasicModel
from django.db import models


class Photo(BasicModel):
    photo = models.ImageField(upload_to='img', null=True)
    slot = models.ForeignKey('Slot', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
