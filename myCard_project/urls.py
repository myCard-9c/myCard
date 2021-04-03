# myCard_project URL Configuration
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myCard import views

urlpatterns = [
    # This maps any URLs starting with rango/ to be handled by rango.
    path('myCard/', include('myCard.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
