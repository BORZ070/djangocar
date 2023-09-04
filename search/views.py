from django.shortcuts import render
from mainpage_car.models import Car, Body, Brand, Transmission, Manufacture


def search_views(request):

    query = request.GET.get('text')
    body_type_id = request.GET.get('body_id')
    transmission_type_id = request.GET.get('transmission')
    country_type_id = request.GET.get('country')
    min_price = request.GET.get('min')
    print("min_price",min_price )
    max_price = request.GET.get('max')

    bodys = Body.objects.all()
    brands = Brand.objects.all()
    transmissions = Transmission.objects.all()
    countrys = Manufacture.objects.all()

    if query:
        cars = Car.objects.filter(brand__icontains=query)
    else:
        cars = Car.objects.all()

    if body_type_id:
        cars = cars.filter(body=body_type_id)

    if transmission_type_id:
        cars = cars.filter(transmission=transmission_type_id)

    if country_type_id:
        cars = cars.filter(manufacture=country_type_id)

    if min_price:
        cars = cars.filter(price__gte=min_price)

    if max_price:
        cars = cars.filter(price__lte=max_price)

    return render(request, 'search.html', {'cars': cars, 'bodys':bodys, 'brands':brands, 'transmissions':transmissions,
                                           'countrys':countrys})

