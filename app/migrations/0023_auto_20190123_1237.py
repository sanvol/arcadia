# Generated by Django 2.1.3 on 2019-01-23 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20190122_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='scoreDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 12, 37, 37, 764311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gamestate',
            name='saveDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 12, 37, 37, 763876, tzinfo=utc)),
        ),
    ]
