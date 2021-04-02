from django.shortcuts import render, redirect
from django.http import HttpResponse
from myCard.forms import UserForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    # Return the response
    return render(request, 'myCard/homepage.html')

def public_cards(request):
    # Return the response
    return render(request, 'myCard/public_cards.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('myCard:index'))
            else:
                return HttpResponse("Your myCard account has been disabled. Please contact Technical Support.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'myCard/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('myCard:index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'myCard/register.html', context = {'user_form' : user_form, 'registered' : registered})

def dashboard(request):
    # Return the response
    return render(request, 'myCard/dashboard.html')

def create_card(request):
    # Return the response
    return render(request, 'myCard/create_card.html')
