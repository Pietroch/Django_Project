from django.db import models

# Create your models here.

class Character(models.Model):
    last_name = models.fields.CharField(max_length=100)
    first_name = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
