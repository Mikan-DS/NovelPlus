import typing

from django.db import models

from users.models import User


class ItemDataCollection(models.Model):
    name = models.CharField(max_length=12, primary_key=True)
    verbose = models.CharField(max_length=20)

    def __str__(self):
        return self.verbose

    class Meta:
        ordering = ('verbose',)
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class ItemDataStatus(models.Model):
    name = models.CharField(max_length=12, primary_key=True)
    verbose = models.CharField(max_length=20)

    def __str__(self):
        return self.verbose

    class Meta:
        ordering = ('verbose',)
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ItemData(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Главное изображение')
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(max_length=256, verbose_name='Краткое описание')
    preview = models.ImageField(upload_to='images/previews/', verbose_name='Превью')

    collection = models.ForeignKey(
        ItemDataCollection,
        on_delete=models.CASCADE,
        verbose_name='Коллекция',
        related_name='items'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')

    status = models.ForeignKey(ItemDataStatus, on_delete=models.CASCADE, verbose_name='Статус')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True)

    is_passed_moderation = models.BooleanField(default=False, verbose_name='Прошло модерацию')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Информационный объект'
        verbose_name_plural = 'Информационные объекты'

    def __str__(self):
        return f'{self.collection.verbose} "{self.title}" ({self.author.username})'

    @property
    def dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image.url,
            "description": self.description,
            "shortDescription": self.short_description,
            "preview": self.preview.url,
            "createdAt": self.created_at.timestamp(),
            "updatedAt": self.updated_at.timestamp(),
        }

    @property
    def item_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        return {
            "image": self.image.url,
            "title": self.title,
            "shortDescription": self.short_description,
            "description": self.description,
        }


    @property
    def card_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        return {
            "id": self.id,
            "title": self.title,
            "preview": self.preview.url
        }

    @property
    def mini_card_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        card = self.card_dict
        card.update({
            "status": self.status.verbose,
            "updatedAt": self.updated_at.timestamp(),
            "shortDescription": self.short_description
        })

        return {
            "id": self.id,
            "title": self.title,
            "preview": self.preview.url
        }

