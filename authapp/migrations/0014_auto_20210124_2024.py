# Generated by Django 2.2.17 on 2021-01-24 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20210124_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 26, 17, 24, 21, 607167, tzinfo=utc)),
        ),
    ]
