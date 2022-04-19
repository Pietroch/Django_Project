from django.contrib import admin

# Register your models here.

from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email')
    
admin.site.register(User, UserAdmin)