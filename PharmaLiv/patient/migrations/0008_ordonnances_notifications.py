# Generated by Django 2.0 on 2018-04-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_ordonnances_medecin'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordonnances',
            name='notifications',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
