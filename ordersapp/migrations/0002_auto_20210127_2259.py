# Generated by Django 2.2.17 on 2021-01-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен'), ('PRD', 'обрабатывается'), ('PD', 'оплачен'), ('RDY', 'готов к выдаче'), ('DN', 'выдан'), ('CNC', 'отменен')], default='FM', max_length=3, verbose_name='статус'),
        ),
    ]
