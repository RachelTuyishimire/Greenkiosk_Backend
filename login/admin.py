from django.contrib import admin
from .models import Login

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ("email", "password")
    
admin.site.register(Login,LoginAdmin)
