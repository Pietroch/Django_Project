# Generated by Django 3.2.13 on 2022-04-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0003_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cote', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cote', models.CharField(max_length=100)),
            ],
        ),
    ]