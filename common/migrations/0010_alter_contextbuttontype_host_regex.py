# Generated by Django 4.2.16 on 2024-11-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_itemdata_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextbuttontype',
            name='host_regex',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
