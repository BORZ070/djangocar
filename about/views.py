from django.shortcuts import render
from about.models import Manager


def about_views(request):
    managers = Manager.objects.all()
    return render(request, 'about.html', {'managers':managers})


def contact_views(request):
    return render(request, 'contact.html')