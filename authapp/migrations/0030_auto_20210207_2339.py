# Generated by Django 2.2.17 on 2021-02-07 20:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0029_auto_20210207_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 39, 23, 777502, tzinfo=utc)),
        ),
    ]