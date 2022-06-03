from django.contrib import admin

# Register your models here.

from travel.models import Trip, Adresse, Activity, Place, PlaceCategory, City
from archives.models import Country

class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end')
    
admin.site.register(Trip, TripAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country')
    
admin.site.register(City, CityAdmin)
class AdresseAdmin(admin.ModelAdmin):
    list_display = ('street', 'numero', 'city')
    
admin.site.register(Adresse, AdresseAdmin)

class PlaceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
admin.site.register(PlaceCategory, PlaceCategoryAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'adresse', 'category')
    
admin.site.register(Place, PlaceAdmin)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('trip', 'category', 'date_start', 'time_start', 'date_end', 'time_end', 'place')
    
admin.site.register(Activity, ActivityAdmin)
