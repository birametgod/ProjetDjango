# Generated by Django 2.0.3 on 2018-04-09 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_femme'),
        ('livreur', '0005_notificationslivreur_livree'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationslivreur',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
            preserve_default=False,
        ),
    ]
