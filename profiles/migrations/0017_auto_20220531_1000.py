# Generated by Django 3.2.13 on 2022-05-31 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_transmission_notaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('heraldry', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='fonction',
            name='entite',
        ),
        migrations.DeleteModel(
            name='Entite',
        ),
        migrations.AddField(
            model_name='fonction',
            name='domaine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.domaine'),
        ),
    ]