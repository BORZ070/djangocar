from django.urls import path, include
from about.views import about_views, contact_views

app_name = 'about'

urlpatterns = [
    path('', about_views, name='about'),
    path('contact/', contact_views, name='contact')
]