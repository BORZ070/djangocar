from django.shortcuts import render
from about.models import Manager
from mainpage_car.models import RateUSD


def about_views(request):
    managers = Manager.objects.all()
    title = 'Plaza car | About us'

    kurs_from_db = RateUSD.objects.last()


    return render(request, 'about.html', {'managers':managers, 'title':title, 'rate':kurs_from_db.rate})


def contact_views(request):
    title = 'Plaza car | Contacts'

    kurs_from_db = RateUSD.objects.last()

    return render(request, 'contact.html', {'title':title, 'rate':kurs_from_db.rate})