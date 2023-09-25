from django.shortcuts import render
from about.models import Manager


def about_views(request):
    managers = Manager.objects.all()
    title = 'Plaza car | About us'
    return render(request, 'about.html', {'managers':managers, 'title':title})


def contact_views(request):
    title = 'Plaza car | Contacts'
    return render(request, 'contact.html', {'title':title})