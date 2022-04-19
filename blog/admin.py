from django.contrib import admin

# Register your models here.

from blog.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'uploader', 'date_created')
    
admin.site.register(Photo, PhotoAdmin)