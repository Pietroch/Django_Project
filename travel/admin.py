from django.contrib import admin

# Register your models here.

from travel.models import Trip, Adresse, Activity

class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end')
    
admin.site.register(Trip, TripAdmin)

class AdresseAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'country')
    
admin.site.register(Adresse, AdresseAdmin)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('trip', 'category', 'date_start', 'date_end', 'adresse')
    
admin.site.register(Activity, ActivityAdmin)
