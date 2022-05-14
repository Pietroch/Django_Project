# Generated by Django 3.2.13 on 2022-05-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0011_document_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('newspaper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archives.newspaper')),
            ],
        ),
    ]
