from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.utils import CustonAccountManager


class Account(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField()
    username = None
    data_joined = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustonAccountManager()
