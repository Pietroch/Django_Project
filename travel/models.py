from django.db import models
from datetime import date
from profiles.models import Character
from archives.models import Country

# Create your models here.

class Adresse(models.Model):
    libelle = models.fields.CharField(max_length=100)
    numero = models.fields.IntegerField(null=True)
    street = models.fields.CharField(max_length=100)
    code = models.fields.IntegerField(null=True)
    city = models.fields.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
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
    TRANSPORT = 'TRANSPORT'
    HEBERGEMENT = 'HEBERGEMENT'
    RESTAURATION = 'RESTAURATION'
    LOISIR = 'LOISIR'

    ROLE_CHOICES = (
        (TRANSPORT, 'Transport'),
        (HEBERGEMENT, 'Hébergement'),
        (RESTAURATION, 'Restauration'),
        (LOISIR, 'Loisir'),
    )
    category = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='catégorie')
    trip = models.ForeignKey(Trip, null=True, blank=True, on_delete=models.SET_NULL)
    adresse = models.ForeignKey(Adresse, null=True, blank=True, on_delete=models.SET_NULL)
    date_start = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today)
    class Meta:
        verbose_name_plural = "Activities"