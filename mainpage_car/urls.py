from django.urls import path
from mainpage_car.views import main_views, detail_views

app_name = 'mainpage_car'

urlpatterns = [
    path('', main_views, name='indexpage'),
    path('car/<int:pk>', detail_views, name='detailpage')

]