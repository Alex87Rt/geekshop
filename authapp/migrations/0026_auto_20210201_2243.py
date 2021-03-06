# Generated by Django 2.2.17 on 2021-02-01 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0025_auto_20210201_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 19, 43, 42, 632030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18, null=True, verbose_name='возраст'),
        ),
    ]
