# Generated by Django 3.2.13 on 2022-05-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0020_alter_activity_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel.trip'),
        ),
    ]