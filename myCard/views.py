from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from myCard.forms import NewUserForm, CardForm
from myCard.models import Card

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

def resume_tips(request):
    # Return the response
    return render(request, 'myCard/resume_tips.html')

def register(request):
    # If the requesti is POST, proceed creating a new user and logging them in
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful." )
            return redirect("myCard:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    # Return the response
    return render (request=request, template_name="myCard/register.html", context={"register_form":form})

def user_login(request):
    # If the requesti is POST, proceed authenticating the user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('myCard:index'))
        else:
            messages.info(request, "Username or password is incorrect.")
    # Return the response
    return render(request, 'myCard/login.html')

@login_required
def user_logout(request):
    logout(request)
    # Return the response
    return redirect(reverse('myCard:index'))

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
    # If the requesti is POST, proceed creating a new Card
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            messages.success(request, "Card created successful." )
            return redirect("myCard:dashboard")
        messages.error(request, "Unsuccessful card creation. Invalid information.")
    form = CardForm
    # Return the response
    return render (request=request, template_name="myCard/create_card.html", context={"card_form":form})

@login_required
def edit_card(request):
    # Return the response
   return render(request, 'myCard/edit_card.html')


class generate_card(View):
    def get(self, request):
        card = Card.objects.get(id=int(request.GET['card_Id']))
        return render(request, 'myCard/card.html',context = {'card':card})

@login_required
def your_card(request):
    card = Card.objects.get(name='Card_name')
    context_dict = {}
    context_dict["card"] = card
    # Return the response
    return render(request, 'myCard/your_card.html')
