from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Country, Depot, Newspaper, Serie, Fond, Document, Issue

from archives import forms

@login_required
def inventaire(request):
    countrys = Country.objects.all
    template = 'archives/inventaire.html'
    context = {
        'countrys': countrys,
        }
    return render(request, template, context)

@login_required
def document_detail(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    fonds = Fond.objects.all()
    series = Serie.objects.all()
    template = 'archives/document_detail.html'
    context = {
        'document' : document,
        'fonds': fonds,
        'series': series,
        }
    return render(request, template, context)

@login_required
def newspaper_list(request):
    newspapers = Newspaper.objects.all()
    template = 'archives/press.html'
    context = {
        'newspapers': newspapers
        }
    return render(request, template, context)

@login_required
def archive_registration(request):
    depot_form = forms.DepotForm()
    if request.method == 'POST':
        depot_form = forms.DepotForm(request.POST)
        if all([depot_form.is_valid()]):
            depot = depot_form.save(commit=False)
            depot.save()
    context = {
        'depot_form': depot_form,
    }
    return render(request, 'archives/archive_registration.html', context=context)




from dal import autocomplete

from archives.models import Country


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


