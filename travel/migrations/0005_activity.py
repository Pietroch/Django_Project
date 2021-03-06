# Generated by Django 3.2.13 on 2022-04-15 08:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20220415_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TRANSPORT', 'Transport'), ('HEBERGEMENT', 'Hébergement'), ('RESTAURATION', 'Restauration'), ('LOISIR', 'Loisir')], max_length=30, verbose_name='catégorie')),
                ('date_start', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(default=datetime.date.today)),
                ('addresse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel.adresse')),
                ('trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel.trip')),
            ],
        ),
    ]
