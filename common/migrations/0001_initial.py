# Generated by Django 4.2.16 on 2024-09-14 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDataCollection',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('verbose', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
                'ordering': ('verbose',),
            },
        ),
        migrations.CreateModel(
            name='ItemDataStatus',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('verbose', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ('verbose',),
            },
        ),
        migrations.CreateModel(
            name='ItemData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Главное изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('short_description', models.TextField(max_length=256, verbose_name='Краткое описание')),
                ('preview', models.ImageField(upload_to='images/previews/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='common.itemdatacollection', verbose_name='Коллекция')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.itemdatastatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Информационный объект',
                'verbose_name_plural': 'Информационные объекты',
                'ordering': ('-created_at',),
            },
        ),
    ]
