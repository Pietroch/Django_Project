from django import forms

from . import models

class DocumentForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text="Title")
    serie = forms.ModelChoiceField(queryset=models.Serie.objects.all(), required=False, help_text="Serie")
    fond = forms.ModelChoiceField(queryset=models.Fond.objects.all().select_related('serie'), required=False, help_text="Fond")


    class Meta:
        model = models.Document
        fields = ['serie', 'fond', 'title']