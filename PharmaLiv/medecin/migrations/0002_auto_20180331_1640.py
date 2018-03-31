# Generated by Django 2.0 on 2018-03-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='hopital',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medecin',
            name='profil',
            field=models.ImageField(blank=True, default='medecin.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='medecin',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medecin',
            name='telephone',
            field=models.IntegerField(default=1, max_length=9),
            preserve_default=False,
        ),
    ]
