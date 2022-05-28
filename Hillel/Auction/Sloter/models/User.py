from django.db import models
# from phone_field import PhoneField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .BasicModel import BasicModel
import jwt
import datetime
from django.conf import settings
from .UserManager import UserManager


class User(BasicModel, AbstractBaseUser, PermissionsMixin):
    class Meta:
        swappable = 'AUTH_USER_MODEL'

    username = models.CharField(db_index=True, max_length=255, unique=True, null=True)
    surname = models.CharField(null=False, max_length=50, default="Ivanov")
    patronymic = models.CharField(null=True, max_length=50, default="Ivanovich")
    email = models.EmailField(null=False, default='owner@mail.com', unique=True)
    birthday = models.DateField(null=False, default=timezone.now)
    # phone_number = PhoneField(blank=True, E164_only=False, null=False, default='+12223334444')
    # Коммит нужный в дальнейшем это будет использовать, но возникла проблема, мы ее решим по мере разработки

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = timezone.now() + datetime.timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def __str__(self):
        return f"{self.id} {self.name}"

