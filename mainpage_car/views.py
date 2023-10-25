import requests
from django.shortcuts import render

from mainpage_car.models import Car, RateUSD
from about.models import Bill

import time


from django.core.mail import send_mail
import asyncio


def main_views(request):
    cars = Car.objects.order_by('?')[:6]
    title = 'Plaza car'
    # time.sleep(2)
    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    usd_rate = data['rates']['USD']
    rate = round(1/usd_rate, 2)
    # save_rate_database
    kurs = RateUSD.objects.last()
    kurs.rate = rate
    kurs.save()
    # load rate from database
    kurs_from_db = RateUSD.objects.last()

    return render(request, 'index_new.html', {'cars': cars, 'title':title, 'rate':kurs_from_db.rate})


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

    kurs_from_db = RateUSD.objects.last()

    return render(request, 'detail_new.html', {'car': car, 'success_message': success_message,
                                               'title': title, 'rate':kurs_from_db.rate})

