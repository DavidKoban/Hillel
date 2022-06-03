from .BasicModel import BasicModel
from django.db import models


class ImageLibrary(BasicModel):
    slot = models.OneToOneField('Slot', on_delete=models.CASCADE)


class Photo(BasicModel):
    photo = models.ImageField(upload_to='img', null=True)
    image_library = models.ForeignKey(ImageLibrary, on_delete=models.CASCADE)
