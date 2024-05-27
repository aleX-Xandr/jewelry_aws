from django.contrib.auth.models import AbstractUser
from django.db import models

from jewelry.models import BaseModel


class User(AbstractUser, BaseModel):
    username = models.CharField("Username", max_length=150, unique=True,)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
