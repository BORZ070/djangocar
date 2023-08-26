from django.shortcuts import render
from mainpage_car.models import Car


def search_views(request, body_id=0):

    query = request.GET.get('text')
    if query:
        cars = Car.objects.filter(brand__icontains=query)
    else:
        cars = Car.objects.all()

    if body_id !=0:
        cars = cars.filter(body=body_id)

    return render(request, 'search.html', {'cars': cars})

