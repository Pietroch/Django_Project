# Generated by Django 3.2.13 on 2022-06-02 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_domaine_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='character',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linkfather', to='profiles.character'),
        ),
        migrations.AddField(
            model_name='character',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linkmother', to='profiles.character'),
        ),
    ]