import typing

from django.db import models

from users.models import User


class ItemDataCollection(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    verbose = models.CharField(max_length=20)

    def __str__(self):
        return self.verbose

    class Meta:
        ordering = ('verbose',)
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class ItemDataStatus(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    verbose = models.CharField(max_length=20)

    def __str__(self):
        return self.verbose

    class Meta:
        ordering = ('verbose',)
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ItemData(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Главное изображение', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(max_length=256, verbose_name='Краткое описание')
    preview = models.ImageField(upload_to='images/previews/', verbose_name='Превью', null=True, blank=True)

    collection = models.ForeignKey(
        ItemDataCollection,
        on_delete=models.CASCADE,
        verbose_name='Коллекция',
        related_name='items'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')

    status = models.ForeignKey(ItemDataStatus, on_delete=models.CASCADE, verbose_name='Статус')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)

    is_passed_moderation = models.BooleanField(default=False, verbose_name='Прошло модерацию')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Информационный объект'
        verbose_name_plural = 'Информационные объекты'

    def __str__(self):
        author = ""
        if self.author:
            author = f" ({self.author.username})"
        else:
            author = " (Archive)"
        return f'{self.collection.verbose} "{self.title}"{author}'

    @property
    def dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        return {
            "id": self.id,
            "title": self.title,
            "image": None if not self.image else self.image.url,
            "description": self.description,
            "shortDescription": self.short_description,
            "preview": None if not self.preview else self.preview.url,
            "createdAt": self.created_at.timestamp(),
            "updatedAt": self.updated_at.timestamp(),
        }

    @property
    def item_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:

        context_buttons = [{"name": cb.button_type.verbose, "url": cb.url} for cb in self.context_buttons.all()]

        author = None
        if self.author:
            author = self.author.id

        return {
            "id": self.id,
            "image": None if not self.image else self.image.url,
            "title": self.title,
            "shortDescription": self.short_description,
            "description": self.description,
            "author": author,
            "contextButtons": context_buttons
        }

    @property
    def card_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        return {
            "id": self.id,
            "title": self.title,
            "preview": None if not self.preview else self.preview.url
        }

    @property
    def mini_card_dict(self) -> typing.Dict[str, typing.Union[str, int, float, None]]:
        card = self.card_dict
        card.update({
            "status": self.status.verbose,
            "updatedAt": self.updated_at.timestamp(),
            "shortDescription": self.short_description
        })

        return card


class ContextButtonType(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    verbose = models.CharField(max_length=20)

    host_regex = models.CharField(max_length=20, default="", blank=True)

    def __str__(self):
        return self.verbose

    class Meta:
        ordering = ('verbose',)
        verbose_name = 'Тип контекстной кнопки'
        verbose_name_plural = 'Типы контекстных кнопок'


class ItemDataContextButton(models.Model):
    item_data = models.ForeignKey(ItemData,
                                  on_delete=models.CASCADE,
                                  related_name='context_buttons',
                                  verbose_name='Информационный объект'
                                  )
    button_type = models.ForeignKey(
        'common.ContextButtonType',
        on_delete=models.CASCADE,
        related_name='item_data_buttons',
        verbose_name='Тип кнопки'
    )
    url = models.URLField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Контекстная кнопка информационного объекта'
        verbose_name_plural = 'Контекстные кнопки информационных объектов'
        unique_together = ('item_data', 'button_type')

    def __str__(self):
        return f'{self.button_type.verbose} = {self.url}'
