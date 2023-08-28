from django.shortcuts import render
from mainpage_car.models import Car


def search_views(request):

    query = request.GET.get('text')
    body_type_id = request.GET.get('body_id')

    if query:
        cars = Car.objects.filter(brand__icontains=query)
    else:
        cars = Car.objects.all()

    if body_type_id:
        cars = cars.filter(body=body_type_id)


    # if body_id !=0:
    #     cars = cars.filter(body=body_id)

    return render(request, 'search.html', {'cars': cars})

