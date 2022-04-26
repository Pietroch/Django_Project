from django.db import models

# Create your models here.

class Doctor(models.Model):
    last_name = models.fields.CharField(max_length=100)
    first_name = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

