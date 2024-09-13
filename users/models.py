from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class User(AbstractUser):

    objects = UserManager()
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
