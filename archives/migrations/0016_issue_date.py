# Generated by Django 3.2.13 on 2022-05-13 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0015_newspaper_founder'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
