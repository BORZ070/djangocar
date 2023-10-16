from django.contrib import admin
from mainpage_car.models import Car, Manufacture, Body, Transmission, Brand, RateUSD


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'generation', 'manufacture', 'body', 'transmission', )
    list_display_links = ('brand', 'model')

admin.site.register(Car, CarAdmin)
admin.site.register(Brand)
admin.site.register(Manufacture)
admin.site.register(Body)
admin.site.register(Transmission)
admin.site.register(RateUSD)