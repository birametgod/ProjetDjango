# Generated by Django 2.0 on 2018-04-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie', '0006_remove_commandes_effectuees_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandes_effectuees',
            name='ordonnance',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
