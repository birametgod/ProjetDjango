# Generated by Django 2.0 on 2018-04-01 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medecin', '0004_medecin_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='login',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='slug',
        ),
        migrations.AddField(
            model_name='medecin',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
