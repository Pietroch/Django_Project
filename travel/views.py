from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from travel.models import Trip, Adresse, Activity

from profiles.models import Character

@login_required
def travel_list(request):
    travels = Trip.objects.prefetch_related('traveller').all()
    for travel in travels:
        travellers = travel.traveller.all()
    template = 'travel/travel_list.html'
    context = {
        'travels' : travels,
        'travellers' : travellers,      
        }
    return render(request, template, context)

@login_required
def travel_detail(request, travel_id):
    travel = get_object_or_404(Trip, id=travel_id)
    activities = Activity.objects.filter(trip_id=travel_id)
    travellers = travel.traveller.all().order_by("last_name", "first_name")
    template = 'travel/travel_detail.html'
    context = {
        'travel': travel,
        'activities' : activities,
        'travellers' : travellers,
        }
    return render(request, template, context)