from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from travel.models import Trip, Activity, Place

from profiles.models import Character, Transmission

from .models import Country

from django.db.models import Sum

@login_required
def travel_list(request):
    travels = Trip.objects.prefetch_related('traveller').all()
    template = 'travel/travel_list.html'
    context = {
        'travels' : travels, 
        }
    return render(request, template, context)

@login_required
def travel_detail(request, travel_id):
    travel = get_object_or_404(Trip, id=travel_id)
    activities = Activity.objects.filter(trip_id=travel_id)
    travellers = travel.traveller.all().order_by("last_name", "first_name")
    prices = Activity.objects.aggregate(Sum('price'))
    template = 'travel/travel_detail.html'
    context = {
        'travel': travel,
        'activities' : activities,
        'travellers' : travellers,
        'prices' : prices,
        }
    return render(request, template, context)

@login_required
def place_list(request):
    countrys = Country.objects.all
    template = 'travel/place_list.html'
    context = {
        'countrys': countrys,
        }
    return render(request, template, context)


@login_required
def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    activities = Activity.objects.filter(place=place_id)
    transmissions = Transmission.objects.filter(place=place_id)
    template = 'travel/place_detail.html'
    context = {
        'place': place,
        'activities': activities,
        'transmissions': transmissions,
        }
    return render(request, template, context)