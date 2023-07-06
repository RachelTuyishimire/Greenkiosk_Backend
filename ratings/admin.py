from django.contrib import admin
from .models import Ratings

# Register your models here.

class RatingsAdmin(admin.ModelAdmin):
    list_display = ("product", "description")

admin.site.register(Ratings, RatingsAdmin)
