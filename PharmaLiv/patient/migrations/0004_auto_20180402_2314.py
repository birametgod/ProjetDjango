# Generated by Django 2.0 on 2018-04-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20180402_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordonnances',
            name='libelle',
            field=models.CharField(max_length=255),
        ),
    ]