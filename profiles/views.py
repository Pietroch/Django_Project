from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from profiles.models import Experience, Character, Company

from travel.models import Trip

@login_required
def character_list(request):
    characters = Character.objects.all().order_by("last_name", "first_name")
    template = 'profiles/character_list.html'
    context = {'characters' : characters}
    return render(request, template, context)

@login_required
def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    experiences = Experience.objects.filter(character_id=character_id)
    travels = Trip.objects.filter(traveller=character_id)
    template = 'profiles/character_detail.html'
    context = {
        'character': character,
        'experiences' : experiences,
        'travels' : travels}
    return render(request, template, context)