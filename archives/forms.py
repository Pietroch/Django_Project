from django import forms

from . import models

class DocumentForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text="Title")
    serie = forms.ModelChoiceField(queryset=models.Serie.objects.all(), required=False, help_text="Serie")
    fond = forms.ModelChoiceField(queryset=models.Fond.objects.all(), required=False, help_text="Fond")


    class Meta:
        model = models.Document
        fields = ['serie', 'fond', 'title']

from dal import autocomplete

from django import forms
from archives import models

class DepotForm(forms.ModelForm):
    class Meta:
        model = models.Depot
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete')
        }