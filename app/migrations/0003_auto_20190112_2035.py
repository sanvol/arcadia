# Generated by Django 2.1.3 on 2019-01-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190112_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='inventory',
            field=models.ManyToManyField(blank=True, default=None, to='app.Game'),
        ),
    ]
