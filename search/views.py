from django.shortcuts import render
from mainpage_car.models import Car


def search_views(request):
    query = request.GET.get('text')
    # print(query)
    cars = Car.objects.all()
    # cars = Car.objects.filter(brand__icontains='BMW')

    return render(request, 'search.html', {'cars': cars})

