from django.contrib import admin

# Register your models here.

from archives.models import Country, Depot, Serie, Fond, Document

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abreviation')

admin.site.register(Country, CountryAdmin)

class DepotAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote', 'country')

admin.site.register(Depot, DepotAdmin)

class SerieAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote')

admin.site.register(Serie, SerieAdmin)

class FondAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote', 'serie')

admin.site.register(Fond, FondAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'fond')

admin.site.register(Document, DocumentAdmin)