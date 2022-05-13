# Generated by Django 3.2.13 on 2022-04-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0008_remove_depot_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='depot',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archives.country'),
        ),
    ]