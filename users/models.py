import typing

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    objects = UserManager()

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватарка')
    vk_user_id = models.IntegerField(blank=True, null=True, unique=True, verbose_name="ID VK")
    description = models.TextField(default="", verbose_name='Описание профиля')

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def as_user_info_dict(self) -> dict:
        return {
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'avatar': self.avatar.url if self.avatar else None,
            'isAdmin': self.is_staff,
            'isAuthenticated': True,
            'id': self.id
        }

    def get_user_page_info_dict(self, current_user_id: typing.Union[int, None]) -> dict:
        return {
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'avatar': self.avatar.url if self.avatar else None,
            'description': self.description,
            'isOwner': self.id == current_user_id,
            'dateJoined': self.date_joined.timestamp(),
            'id': self.id
        }
