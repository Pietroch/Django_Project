# Generated by Django 3.2.13 on 2022-04-14 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0005_auto_20220414_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='cote',
            new_name='abreviation',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='title',
            new_name='name',
        ),
    ]
