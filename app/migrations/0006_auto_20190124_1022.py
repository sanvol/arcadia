# Generated by Django 2.1.3 on 2019-01-24 10:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190115_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamestate',
            old_name='game_state',
            new_name='gameState',
        ),
        migrations.RemoveField(
            model_name='game',
            name='highscore',
        ),
        migrations.RemoveField(
            model_name='gamescore',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='gamestate',
            name='settings',
        ),
        migrations.RemoveField(
            model_name='gamestate',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='game',
            name='high_score',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='high_score_in', to='app.GameScore'),
        ),
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='scoreDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='gamestate',
            name='saveDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
