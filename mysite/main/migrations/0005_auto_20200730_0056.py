# Generated by Django 3.0.8 on 2020-07-29 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200730_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 0, 56, 4, 218547), verbose_name='date published'),
        ),
    ]
