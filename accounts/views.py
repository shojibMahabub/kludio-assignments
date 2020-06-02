from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from.models import *
from.forms import CreateUserForm, CustomerEntryForm

@login_required
def listview(request):
	customer = Customer.objects.all()
	return render(request, 'accounts/list.html', {'customer': customer})

def customer_entry(request):
	if request.method == 'POST':
		form = CustomerEntryForm(request.POST)
		if form.is_valid():
			obj = Customer(
				name = form.cleaned_data.get('name'),
				email = form.cleaned_data.get('email'),
				phone = form.cleaned_data.get('phone')
			)
			obj.save()
			return render(request, 'accounts/success.html')
		else:
			return render(request, 'accounts/entry.html', {'form': form})

	form = CustomerEntryForm()
	context = {
		'form': form
	}
	return render(request, 'accounts/entry.html', context)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('listview')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('listview')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('listview')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

@login_required
def logoutUser(request):
	logout(request)
	return redirect('login')