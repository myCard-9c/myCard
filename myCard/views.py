from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # Return the response
    return render(request, 'myCard/homepage.html')

def public_cards(request):
    # Return the response
    return render(request, 'myCard/public_cards.html')
