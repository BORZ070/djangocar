import requests
from django.shortcuts import render
from mainpage_car.models import Car
from about.models import Bill
from django.core.mail import send_mail
import time

def main_views(request):
    cars = Car.objects.order_by('?')[:6]
    title = 'Plaza car'
    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    usd_rate = data['rates']['USD']
    rate = round(1/usd_rate, 2)
    return render(request, 'index_new.html', {'cars': cars, 'title':title, 'rate':rate})


def detail_views(request, pk):
    car = Car.objects.get(id=pk)
    success_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        manager_email = car.manager.email

        bill = Bill(email=email, name=name, comment=comment, manager_email=manager_email)
        bill.save()
        success_message = 'Заявка отправлена!'
    title = f'{car.brand} | {car.model}'
    return render(request, 'detail_new.html', {'car': car, 'success_message': success_message,
                                               'title': title})

