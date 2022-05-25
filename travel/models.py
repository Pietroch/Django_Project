from django.db import models
from datetime import date
from profiles.models import Character

# Create your models here.

class Adresse(models.Model):
    numero = models.fields.IntegerField(null=True, blank=True)
    street = models.fields.CharField(max_length=100, null=True, blank=True)
    code = models.fields.IntegerField(null=True)
    city = models.fields.CharField(max_length=100, null=True)
    country = models.fields.CharField(max_length=100, null=True)
    def __str__(self):
        return f'{self.numero} {self.street}, {self.code} {self.city}'

class PlaceCategory(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'
        
class Place(models.Model):
    name = models.fields.CharField(max_length=100)
    adresse = models.ForeignKey(Adresse, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(PlaceCategory, null=True, on_delete=models.SET_NULL)
    description = models.fields.CharField(max_length=100, null=True, blank=True)
    latitude = models.fields.DecimalField(max_digits = 10, decimal_places = 10, null=True, blank=True)
    longitude = models.fields.DecimalField(max_digits = 10, decimal_places = 10, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

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
    trip = models.ForeignKey(Trip, null=True, blank=True, on_delete=models.SET_NULL)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)
    date_start = models.DateField(default=date.today)
    time_start = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    date_end = models.DateField(default=date.today)
    time_end = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    visitor = models.ManyToManyField(Character)
    class Meta:
        verbose_name_plural = "Activities"