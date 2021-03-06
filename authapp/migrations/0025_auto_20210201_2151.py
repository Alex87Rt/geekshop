# Generated by Django 2.2.17 on 2021-02-01 18:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0024_auto_20210128_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuserprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=512, verbose_name='обо мне'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 18, 51, 26, 644343, tzinfo=utc)),
        ),
    ]
