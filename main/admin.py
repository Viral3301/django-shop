from django.contrib import admin
from .models import Category,Vehicles,Accessories
# Register your models here.

@admin.register(Vehicles)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['title','manufacturer','year']

@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['title','manufacturer']


admin.site.register(Category)