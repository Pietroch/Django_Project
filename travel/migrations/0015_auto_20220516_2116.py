# Generated by Django 3.2.13 on 2022-05-16 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20220516_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='adresse',
        ),
        migrations.AddField(
            model_name='activity',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel.place'),
        ),
    ]
