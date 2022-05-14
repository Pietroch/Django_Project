from django.contrib import admin

# Register your models here.

from archives.models import Country, Depot, Serie, Fond, Document, Newspaper, Issue

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abreviation')

admin.site.register(Country, CountryAdmin)

class DepotAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote', 'country')

admin.site.register(Depot, DepotAdmin)

class SerieAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote', 'depot')

admin.site.register(Serie, SerieAdmin)

class FondAdmin(admin.ModelAdmin):
    list_display = ('title', 'cote', 'serie', 'get_depot')
    @admin.display(description='Dépôt', ordering='serie__depot')
    def get_depot(self, obj):
        return obj.serie.depot

admin.site.register(Fond, FondAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'fond', 'get_serie')
    @admin.display(description='Serie', ordering='fond__serie')
    def get_serie(self, obj):
        return obj.fond.serie

admin.site.register(Document, DocumentAdmin)

class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'frequency', 'kind', 'language')

admin.site.register(Newspaper, NewspaperAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display = ('newspaper','number', 'date')

admin.site.register(Issue, IssueAdmin)