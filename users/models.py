import typing

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    objects = UserManager()

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватарка')
    vk_user_id = models.IntegerField(blank=True, null=True, unique=True, verbose_name="ID VK")
    description = models.TextField(default="", verbose_name='Описание профиля', blank=True)

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

    @property
    def as_common_info_dict(self) -> dict:
        return {
            'username': self.username,
            'firstName': self.first_name,
            'avatar': self.avatar.url if self.avatar else None,
            'id': self.id
        }

    def get_user_page_info_dict(self, current_user_id: typing.Union[int, None]) -> dict:

        context_buttons = [{"name": cb.button_type.verbose, "url": cb.url} for cb in self.context_buttons.all()]

        return {
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'avatar': self.avatar.url if self.avatar else None,
            'description': self.description,
            'isOwner': self.id == current_user_id,
            'dateJoined': self.date_joined.timestamp(),
            'id': self.id,
            'contextButtons': context_buttons
        }


class UserContextButton(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='context_buttons',
                             verbose_name='Пользователь'
                             )
    button_type = models.ForeignKey(
        'common.ContextButtonType',
        on_delete=models.CASCADE,
        related_name='user_buttons',
        verbose_name='Тип кнопки'
    )
    url = models.URLField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Контекстная кнопка пользователей'
        verbose_name_plural = 'Контекстные кнопки пользователей'
        unique_together = ('user', 'button_type')

    def __str__(self):
        return f'{self.button_type.verbose} = {self.url}'
