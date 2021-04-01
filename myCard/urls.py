from django.urls import path
from myCard import views

app_name = 'myCard'

urlpatterns = [
    path('', views.index, name='index'),
    path('public_cards/', views.public_cards, name='public_cards'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
