# Generated by Django 2.2.17 on 2021-02-11 20:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0044_auto_20210211_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 13, 20, 5, 11, 60714, tzinfo=utc)),
        ),
    ]
