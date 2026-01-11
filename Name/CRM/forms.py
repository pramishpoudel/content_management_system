from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Record

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecordForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=15)
    city = forms.CharField(required=True, max_length=100)
    country = forms.CharField(required=True, max_length=100)
    state = forms.CharField(required=True, max_length=100)
    zip_code = forms.CharField(required=True, max_length=20)

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'country', 'state', 'zip_code']