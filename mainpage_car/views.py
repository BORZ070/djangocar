from django.shortcuts import render
from mainpage_car.models import Car
from about.models import Bill


def main_views(request):
    cars = Car.objects.order_by('?')[:6]
    return render(request, 'index_new.html', {'cars': cars})


def detail_views(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        form = Bill(request.POST)
        email = form.cleaned_data['email']
        print(email, 'email')
        name = form.cleaned_data['name']
        print(name, 'name')
    else:
        form = Bill()
    return render(request, 'detail_new.html', {'car': car})

