# Generated by Django 3.2.13 on 2022-04-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmanagement', '0006_alter_db_software'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='file',
            field=models.FileField(upload_to='db/'),
        ),
    ]
