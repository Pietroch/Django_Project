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
        'countrys': countrys,}
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
        'series': series}
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
    document_form = forms.DocumentForm()
    if request.method == 'POST':
        document_form = forms.DocumentForm(request.POST)
        if all([document_form.is_valid()]):
            document = document_form.save(commit=False)
            document.save()
    context = {
        'document_form': document_form,
    }
    return render(request, 'archives/archive_registration.html', context=context)