from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

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
