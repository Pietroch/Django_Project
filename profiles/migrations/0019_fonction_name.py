# Generated by Django 3.2.13 on 2022-05-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_alter_domaine_heraldry'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonction',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]