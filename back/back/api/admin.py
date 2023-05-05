from django.contrib import admin

# Register your models here.
from api.models import *

# Register your models here.
@admin.register(Products)
class Product(admin.ModelAdmin):
    list_display = ("id", "title", "price", "year", "image", "configure", "quantity", "trash")