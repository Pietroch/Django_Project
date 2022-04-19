from django import forms

from . import models

class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = ['name', 'abreviation']

class DepotForm(forms.ModelForm):
    class Meta:
        model = models.Depot
        fields = ['title', 'cote']