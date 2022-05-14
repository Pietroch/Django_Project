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
    date_birth = models.DateField(default=date.today, null=True, blank=True)
    date_death = models.DateField(default=date.today, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Event(models.Model):
    kind = models.fields.CharField(max_length=100)
    date = models.DateField(default=date.today, null=True, blank=True)
    def __str__(self):
        return f'{self.kind}'

class Company(models.Model):
    name = models.fields.CharField(max_length=100)
    location = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = "Compagnies"

class Experience(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    position = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.position} chez {self.company}'
