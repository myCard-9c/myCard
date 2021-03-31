# myCard_project URL Configuration

from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from myCard import views

urlpatterns = [
    # This maps any URLs starting with rango/ to be handled by rango.
    path('myCard/', include('myCard.urls')),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
