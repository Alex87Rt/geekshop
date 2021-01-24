# Generated by Django 2.2.17 on 2021-01-22 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210123_0005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='ShopUserProfile',
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 24, 21, 13, 44, 794999, tzinfo=utc)),
        ),
    ]
