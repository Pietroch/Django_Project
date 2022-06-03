from django.db import models
from datetime import date

# Create your models here.
class Character(models.Model):
    H = 'Male'
    F = 'Female'
    GENDER_CHOICES = (
        (H, 'Male'),
        (F, 'Female'),
    )
    
    last_name = models.fields.CharField(max_length=100)
    first_name = models.fields.CharField(max_length=100)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    mother = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='linkmother', limit_choices_to={'gender': F})
    father = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='linkfather', limit_choices_to={'gender': H})
    date_birth = models.DateField(null=True, blank=True)
    date_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Company(models.Model):
    name = models.fields.CharField(max_length=100)
    location = models.fields.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Compagnies"
    def __str__(self):
        return f'{self.name}'
    

class Experience(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    position = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.position} chez {self.company}'

class Title(models.Model):
    identifiant = models.fields.CharField(max_length=100)
    masculin = models.fields.CharField(max_length=100)
    feminin = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.identifiant}'

class Domaine(models.Model):
    pluriel = 'pluriel'
    feminin = 'féminin'
    masculin = 'masculin'
    voyelle = 'voyelle'
    GENDER_CHOICES = (
        (pluriel, 'pluriel'),
        (feminin, 'féminin'),
        (masculin, 'masculin'),
        (voyelle, 'voyelle'),
    )
    name = models.fields.CharField(max_length=100)
    heraldry = models.fields.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Fonction(models.Model):
    title = models.ForeignKey(Title, null=True, blank=True, on_delete=models.SET_NULL)
    character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    domaine = models.ForeignKey(Domaine, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.fields.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f'{self.title} de {self.domaine}'

from travel.models import Place
class Transmission(models.Model):
    kind = models.fields.CharField(max_length=100)
    date = models.DateField(default=date.today, null=True, blank=True)
    notaire = models.ManyToManyField(Character, related_name='linknotaire')
    place = models.ManyToManyField(Place)
    vendeur = models.ManyToManyField(Character, related_name='linkvendeur')
    acheteur = models.ManyToManyField(Character, related_name='linkacheteur')
    def __str__(self):
        return f'{self.kind} le {self.date}'

