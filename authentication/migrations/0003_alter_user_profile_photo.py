# Generated by Django 3.2.13 on 2022-04-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20220413_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo de profil'),
        ),
    ]
