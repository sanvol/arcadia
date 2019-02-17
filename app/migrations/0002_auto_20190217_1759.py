# Generated by Django 2.1.7 on 2019-02-17 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='high_score',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='high_score_in', to='app.GameScore'),
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Game'),
        ),
    ]
