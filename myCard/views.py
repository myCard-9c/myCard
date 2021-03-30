from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # Return the response with cookies updated
    return render(request, 'myCard/homepage.html')
