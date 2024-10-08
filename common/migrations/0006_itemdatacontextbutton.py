# Generated by Django 4.2.16 on 2024-10-02 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_contextbuttontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDataContextButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='Ссылка')),
                ('button_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_data_buttons', to='common.contextbuttontype', verbose_name='Тип кнопки')),
                ('item_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context_buttons', to='common.itemdata', verbose_name='Информационный объект')),
            ],
            options={
                'verbose_name': 'Контекстная кнопка информационного объекта',
                'verbose_name_plural': 'Контекстные кнопки информационных объектов',
                'unique_together': {('item_data', 'button_type')},
            },
        ),
    ]
