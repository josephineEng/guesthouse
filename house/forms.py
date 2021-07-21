from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class meta:
        model = User
        fields =["username",'first_name', 'last_name',"email","password1","password2"]

class SigninForm(forms.Form):
    service = forms.CharField(label='service', max_length=100)
    day = forms.CharField(label='day of booking', max_length=100)
    contact = forms.CharField(label='your contact', max_length=100)
