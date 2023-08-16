from django.shortcuts import render
from mainpage_car.models import Car


def main_views(request):
    cars = Car.objects.all()
    return render(request, 'index_new.html', {'cars': cars})


def detail_views(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'detail_new.html', {'car': car})
