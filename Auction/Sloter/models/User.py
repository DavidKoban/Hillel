from django.db import models
# from phone_field import PhoneField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .BasicModel import BasicModel


class User(BasicModel, AbstractBaseUser, PermissionsMixin):
    class Meta:
        swappable = 'AUTH_USER_MODEL'


    surname = models.CharField(null=False, max_length=50, default="Ivanov")
    patronymic = models.CharField(null=True, max_length=50, default="Ivanovich")
    password = models.CharField(null=False, max_length=50, default=' ')
    email = models.EmailField(null=False, default='owner@mail.com')
    birthday = models.DateField(null=False, default=timezone.now)
    # phone_number = PhoneField(blank=True, E164_only=False, null=False, default='+12223334444')
    # Коммит нужный в дальнейшем это будет использовать, но возникла проблема, мы ее решим по мере разработки

    def __str__(self):
        return f"{self.id} {self.name}"

