# Generated by Django 2.0 on 2018-04-01 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20180401_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='birth_date',
            new_name='dateNaissance',
        ),
    ]