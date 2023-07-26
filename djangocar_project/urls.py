from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage_car.urls', namespace='mainpage_car'))
]


if settings.DEBUG is True:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)