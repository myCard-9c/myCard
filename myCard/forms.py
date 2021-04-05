from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myCard.models import Card

# Form to gather registration data
class NewUserForm(UserCreationForm):
    # Additional fields to the UserCreationForm
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # Helper class to display fields
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
    # Function to save the User object
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    # Helper function to not display the helper text
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "first_name", "last_name", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None

# Form to gather registration data
class CardForm(forms.ModelForm):
    # Helper class to display fields
    class Meta:
        model = Card
        fields = ('user', 'first_name', 'last_name', 'email', 'phone_no', 'location', 'website', 'occupation', 'name', 'visibility', 'picture')
    # Function to save the Card object
    def save(self, commit=True):
        card = super(CardForm, self).save(commit=True)
        card.user = self.cleaned_data['user']
        card.name = self.cleaned_data['name']
        card.first_name = self.cleaned_data['first_name']
        card.last_name = self.cleaned_data['last_name']
        card.email = self.cleaned_data['email']
        card.phone_no = self.cleaned_data['phone_no']
        card.location = self.cleaned_data['location']
        card.website = self.cleaned_data['website']
        card.occupation = self.cleaned_data['occupation']
        card.visibility = self.cleaned_data['visibility']
        card.picture = self.cleaned_data['picture']
        if commit:
            card.save()
        return card
    # Helper function to not display the helper text
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'email', 'phone_no', 'location', 'website', 'occupation', 'name', 'visibility', 'picture']:
            self.fields[fieldname].help_text = None
