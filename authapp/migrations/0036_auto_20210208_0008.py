# Generated by Django 2.2.17 on 2021-02-07 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0035_auto_20210208_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 21, 8, 3, 902596, tzinfo=utc)),
        ),
    ]
