# Generated by Django 3.2.13 on 2022-04-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20220419_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, null=True),
        ),
    ]
