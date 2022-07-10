# Generated by Django 4.0.3 on 2022-04-10 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(default=datetime.date.today, verbose_name='дата измерения'),
        ),
    ]
