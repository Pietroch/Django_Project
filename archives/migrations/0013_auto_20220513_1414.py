# Generated by Django 3.2.13 on 2022-05-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0012_issue_newspaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='frequency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='kind',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
