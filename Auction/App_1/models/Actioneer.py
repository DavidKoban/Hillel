import uuid
from django.db import models
# from phone_field import PhoneField
from django.utils import timezone


class Auctioneer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=50, default="Ivan")
    surname = models.CharField(null=False, max_length=50, default="Ivanov")
    patronymic = models.CharField(null=True, max_length=50, default="Ivanovich")
    password = models.CharField(null=False, max_length=50, default=' ')
    email = models.EmailField(null=False, default='owner@mail.com')
    birthday = models.DateField(null=False, default=timezone.now)
    # phone_number = PhoneField(blank=True, E164_only=False, null=False, default='+12223334444')
    # Коммит нужный в дальнейшем это будет использовать, но возникла проблема, мы ее решим по мере разработки

    def __str__(self):
        return f"{self.id} {self.name}"
