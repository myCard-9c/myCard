from django.shortcuts import render, redirect
from django.http import HttpResponse
from myCard.forms import UserForm
from myCard.forms import NewUserForm
from myCard.models import Card
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

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
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			messages.success(request, "Registration successful." )
			return redirect("myCard:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="myCard/register.html", context={"register_form":form})

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


def edit_card(request):
   return render(request, 'myCard/edit_card.html')

class generate_card(View):
    def get(self, request):
        card = Card.objects.order_by('id')[0]
        return render(request, 'myCard/card.html',context = {'card':card})

def your_card(request):
    card = Card.objects.get(name='Card_name')
    context_dict = {}
    context_dict["card"] = card

    # Return the response
    return render(request, 'myCard/your_card.html', context_dict)
