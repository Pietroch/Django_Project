from django import forms

from . import models

class DbForm(forms.ModelForm):
    class Meta:
        model = models.Db
        fields = ['file', 'software']
