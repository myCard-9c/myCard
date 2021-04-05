from django.urls import path
from myCard import views

app_name = 'myCard'

# myCard URLs configuration
urlpatterns = [
    path('', views.index, name='index'),
    path('public_cards/', views.public_cards, name='public_cards'),
    path('resume_tips/', views.resume_tips, name='resume_tips'),
    path('register/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_card/', views.create_card, name='create_card'),
    path('generate_card/', views.generate_card.as_view(), name='generate_card'),
]
