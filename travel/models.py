from django.db import models
from datetime import date
from profiles.models import Character

# Create your models here.

class Adresse(models.Model):
    libelle = models.fields.CharField(max_length=100)
    numero = models.fields.IntegerField(null=True, blank=True)
    street = models.fields.CharField(max_length=100)
    code = models.fields.IntegerField(null=True)
    city = models.fields.CharField(max_length=100, null=True)
    country = models.fields.CharField(max_length=100, null=True)
    def __str__(self):
        return f'{self.libelle}'

class Trip(models.Model):
    title = models.fields.CharField(max_length=100)
    traveller = models.ManyToManyField(Character)
    date_start = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today)
    def __str__(self):
        return f'{self.title}'

class Activity(models.Model):
    TRANSPORT = 'Transport'
    HEBERGEMENT = 'Hébergement'
    RESTAURATION = 'Restauration'
    LOISIR = 'Loisir'

    ROLE_CHOICES = (
        (TRANSPORT, 'Transport'),
        (HEBERGEMENT, 'Hébergement'),
        (RESTAURATION, 'Restauration'),
        (LOISIR, 'Loisir'),
    )
    category = models.CharField(max_length=30, choices=ROLE_CHOICES)
    trip = models.ForeignKey(Trip, null=True, on_delete=models.SET_NULL)
    adresse = models.ForeignKey(Adresse, null=True, blank=True, on_delete=models.SET_NULL)
    date_start = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today)
    class Meta:
        verbose_name_plural = "Activities"