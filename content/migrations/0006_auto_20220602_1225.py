# Generated by Django 3.2.13 on 2022-06-02 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20220602_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frnoun',
            name='word',
        ),
        migrations.RemoveField(
            model_name='wordnoun',
            name='noun_ct',
        ),
        migrations.RemoveField(
            model_name='wordnoun',
            name='word',
        ),
        migrations.DeleteModel(
            name='EnNoun',
        ),
        migrations.DeleteModel(
            name='FrNoun',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
        migrations.DeleteModel(
            name='WordNoun',
        ),
    ]
