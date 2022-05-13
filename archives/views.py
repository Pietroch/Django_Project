from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import Country, Depot, Serie, Fond, Document

from archives import forms

@login_required
def inventaire(request):
    documents = Document.objects.all()
    fonds = Serie.objects.filter(id__in=documents)
    series = Serie.objects.filter(id__in=fonds)
    depots = Depot.objects.filter(id__in=series)
    countrys = Country.objects.filter(id__in=depots)
    template = 'archives/inventaire.html'
    context = {
        'countrys': countrys,
        'depots': depots,
        'series': series,
        'fonds': fonds,
        'documents': documents}
    return render(request, template, context)

@login_required
def document_detail(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    fonds = Fond.objects.all()
    series = Serie.objects.all()
    template = 'archives/document_detail.html'
    context = {'document' : document, 'fonds': fonds, 'series': series}
    return render(request, template, context)

@login_required
def archive_registration(request):
    depot_form = forms.DepotForm()
    country_form = forms.CountryForm()
    if request.method == 'POST':
        depot_form = forms.DepotForm(request.POST)
        country_form = forms.CountryForm(request.POST)
        if all([depot_form.is_valid(), country_form.is_valid()]):
            country = country_form.save(commit=False)
            country.save()
            depot = depot_form.save(commit=False)
            depot.country = country
            depot.save()
    context = {
        'depot_form': depot_form,
        'country_form': country_form,
    }
    return render(request, 'archives/archive_registration.html', context=context)