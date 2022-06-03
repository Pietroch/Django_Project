from django.contrib import admin

# Register your models here.

from profiles.models import Company, Experience, Character, Transmission, Domaine, Title, Fonction

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    
admin.site.register(Character, CharacterAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    
admin.site.register(Company, CompanyAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'character')
    
admin.site.register(Experience, ExperienceAdmin)

class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('kind', 'date')

admin.site.register(Transmission, TransmissionAdmin)

class DomaineAdmin(admin.ModelAdmin):
    list_display = ('name', 'heraldry')
    
admin.site.register(Domaine, DomaineAdmin)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'masculin', 'feminin')
    
admin.site.register(Title, TitleAdmin)

class FonctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'character', 'domaine')
    
admin.site.register(Fonction, FonctionAdmin)