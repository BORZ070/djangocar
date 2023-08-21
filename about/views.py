from django.shortcuts import render

def about_views(request):
    return render(request, 'about.html')
