from django.urls import path
from myCard import views

app_name = 'myCard'

urlpatterns = [
    path('', views.index, name='index'),
    path('public_cards/', views.public_cards, name='public_cards'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_card/', views.create_card, name='create_card'),
    path('resume_tips/', views.resume_tips, name='resume_tips'),
    path('edit_card/', views.edit_card, name='edit_card'),
    path('generate_card/', views.generate_card.as_view(), name='generate_card'),
]
