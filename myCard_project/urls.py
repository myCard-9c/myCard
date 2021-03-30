"""myCard_project URL Configuration
"""
from django.urls import path
from myCard import views

app_name = 'myCard'

urlpatterns = [
    path('', views.index, name='index'),
]
