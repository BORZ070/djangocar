from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mainpage_car.views import main_views, detail_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views),
    path('car/<int:pk>', detail_views)
    #path('', include('mainpage_car.urls', namespace='mainpage_car'))
]


if settings.DEBUG is True:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)