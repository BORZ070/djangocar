from django.urls import path, include
from search.views import search_views

app_name = 'search'

urlpatterns = [
    path('', search_views, name='search'),
    path('body/<int:body_id>', search_views, name='body')
]
