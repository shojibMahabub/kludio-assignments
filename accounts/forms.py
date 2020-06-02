from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import *




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerEntryForm(forms.Form):
	name = forms.CharField(max_length=50, required=True)
	email = forms.CharField(max_length=50, required=True)
	phone = forms.CharField(max_length=20, required=True)
	