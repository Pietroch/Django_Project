from django.db import models
from datetime import date
from travel.models import Trip
from profiles.models import Character

class Country(models.Model):
    name = models.fields.CharField(max_length=100)
    abreviation = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = "Countries"

class Depot(models.Model):
    title = models.fields.CharField(max_length=100)
    cote = models.fields.CharField(max_length=100)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'

class Serie(models.Model):
    title = models.fields.CharField(max_length=100)
    cote = models.fields.CharField(max_length=100)
    depot = models.ForeignKey(Depot, null=True, on_delete=models.SET_NULL)
    date = models.IntegerField(null=True, blank=True)
    date_start = models.IntegerField(null=True, blank=True)
    date_end = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.cote} : {self.title}'

class Fond(models.Model):
    title = models.fields.CharField(max_length=100)
    cote = models.fields.CharField(max_length=100)
    serie = models.ForeignKey(Serie, null=True, on_delete=models.SET_NULL)
    date = models.IntegerField(null=True, blank=True)
    date_start = models.IntegerField(null=True, blank=True)
    date_end = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.cote} : {self.title}'

class Document(models.Model):
    title = models.fields.CharField(max_length=100)
    fond = models.ForeignKey(Fond, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True, blank=True)
    language = models.fields.CharField(max_length=100, null=True, blank=True)
    transcription = models.fields.CharField(max_length=5000, null=True, blank=True)
    note = models.fields.CharField(max_length=5000, null=True, blank=True)
    event = models.ForeignKey(Trip, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'

class Newspaper(models.Model):
    title = models.fields.CharField(max_length=100)
    frequency = models.fields.CharField(max_length=100, null=True, blank=True)
    kind = models.fields.CharField(max_length=100, null=True, blank=True)
    language = models.fields.CharField(max_length=100, null=True, blank=True)
    founder = models.ManyToManyField(Character)
    def __str__(self):
        return f'{self.title}'

class Issue(models.Model):
    number = models.IntegerField()
    newspaper = models.ForeignKey(Newspaper, null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=date.today)
    def __str__(self):
        return f'{self.newspaper} - {self.number} - {self.date}'