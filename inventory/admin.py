from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price", "date_created", "date_updated", "image")



admin.site.register(Product, ProductAdmin)

