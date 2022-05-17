from django.contrib import admin

# Register your models here.

from travel.models import Trip, Adresse, Activity, Place

class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end')
    
admin.site.register(Trip, TripAdmin)

class AdresseAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')
    
admin.site.register(Adresse, AdresseAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
admin.site.register(Place, PlaceAdmin)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('trip', 'category', 'date_start', 'date_end', 'place')
    
admin.site.register(Activity, ActivityAdmin)
