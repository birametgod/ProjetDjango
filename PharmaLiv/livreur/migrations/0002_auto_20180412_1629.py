# Generated by Django 2.0 on 2018-04-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livreur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(choices=[('thies', 'Thiès'), ('dakar', 'Dakar'), ('Fatick', 'Fatick'), ('Saint-Louis', 'Saint-Louis'), ('Mbour', 'Mbour'), ('Kaolack', 'Kaolack'), ('Louga', 'Louga')], max_length=10),
        ),
    ]
