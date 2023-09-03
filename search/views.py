from django.shortcuts import render
from mainpage_car.models import Car, Body, Brand, Transmission


def search_views(request):

    query = request.GET.get('text')
    body_type_id = request.GET.get('body_id')
    transmission_type_id = request.GET.get('transmission')

    bodys = Body.objects.all()
    brands = Brand.objects.all()
    transmissions = Transmission.objects.all()

    if query:
        cars = Car.objects.filter(brand__icontains=query)
    else:
        cars = Car.objects.all()

    if body_type_id:
        cars = cars.filter(body=body_type_id)

    if transmission_type_id:
        cars = cars.filter(transmission=transmission_type_id)


    return render(request, 'search.html', {'cars': cars, 'bodys':bodys, 'brands':brands, 'transmissions':transmissions})

