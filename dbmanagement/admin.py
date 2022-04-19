from django.contrib import admin

from dbmanagement.models import Db

class DbAdmin(admin.ModelAdmin):
    list_display = ('file', 'software')

admin.site.register(Db, DbAdmin)
