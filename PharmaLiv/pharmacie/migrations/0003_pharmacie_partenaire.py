# Generated by Django 2.0.3 on 2018-04-04 22:18
# Generated by Django 2.0 on 2018-04-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie', '0002_auto_20180402_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacie',
            name='partenaire',
            field=models.BooleanField(default='1'),
        ),
    ]
