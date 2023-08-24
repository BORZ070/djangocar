from django.shortcuts import render
from mainpage_car.models import Car


def search_views(request):
    query = request.GET.get('text')

    # cars = Car.objects.all()
    cars = Car.objects.filter(brand__icontains=query)

    return render(request, 'search.html', {'cars': cars})

