from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # Return the response
    return render(request, 'myCard/homepage.html')

def public_cards(request):
    # Return the response
    return render(request, 'myCard/public_cards.html')

def login(request):
    # Return the response
    return render(request, 'myCard/login.html')

def signup(request):
    # Return the response
    return render(request, 'myCard/signup.html')

def dashboard(request):
    # Return the response
    return render(request, 'myCard/dashboard.html')

def create_card(request):
    # Return the response
    return render(request, 'myCard/create_card.html')
