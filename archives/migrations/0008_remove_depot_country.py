# Generated by Django 3.2.13 on 2022-04-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0007_alter_country_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depot',
            name='country',
        ),
    ]