from django.contrib import admin
from mainpage_car.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'generation')
    list_display_links = ('brand', 'model')

admin.site.register(Car, CarAdmin)
