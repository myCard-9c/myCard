from django.shortcuts import render, redirect
from django.http import HttpResponse
from myCard.forms import UserForm
from myCard.models import Card
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    # List of the last 3 visible Card
    card_list = Card.objects.order_by('-id').filter(visibility=True)[:3]

    # Costruct a dictionary to pass the template engine as its context.
    context_dict = {}
    context_dict['cards'] = card_list

    # Return the response
    return render(request, 'myCard/homepage.html', context=context_dict)

def public_cards(request):
    # List of the last 3 visible Card
    card_list = Card.objects.filter(visibility=True).order_by('-id')

    # Costruct a dictionary to pass the template engine as its context.
    context_dict = {}
    context_dict['cards'] = card_list

    # Return the response
    return render(request, 'myCard/public_cards.html', context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('myCard:index'))
        else:
            messages.info(request, "Username or password is incorrect.")

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

@login_required
def dashboard(request):
    # List of the user Cards
    card_list = Card.objects.filter(user=request.user)

    # Costruct a dictionary to pass the template engine as its context.
    context_dict = {}
    context_dict['cards'] = card_list

    # Return the response
    return render(request, 'myCard/dashboard.html', context_dict)

@login_required
def create_card(request):
    # Return the response
    return render(request, 'myCard/create_card.html')

def resume_tips(request):
    # Return the response
    return render(request, 'myCard/resume_tips.html')

def your_card(request):
    card = Card.objects.get(name='Card_name')
    context_dict = {}
    context_dict["card"] = card

    # Return the response
    return render(request, 'myCard/your_card.html', context_dict)
