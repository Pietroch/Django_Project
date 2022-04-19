from django.contrib import admin

# Register your models here.

from profiles.models import Company, Experience, Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    
admin.site.register(Character, CharacterAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    
admin.site.register(Company, CompanyAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'character')
    
admin.site.register(Experience, ExperienceAdmin)