from django.shortcuts import render,redirect
from Products.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages,auth

from User.forms import RegistrationForm,AccountAuthenticationForm


# Create your views here.

def home(request):
    products = Products.objects.all()
    for product in products:
        unique_colors = product.variants.values_list('color__color_code', flat=True).distinct()
        product.unique_colors = unique_colors
        print(unique_colors)
    context = {
        'products': products
    }
    return render(request,'home.html',context)

def login(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				auth.login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, "login.html", context)

def register(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			customer = authenticate(email=email, password=raw_password)
			auth.login(request, customer)
			destination = kwargs.get("next")
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    # del request.session['email']
    return redirect(home)



def checkout(request):
    return render(request,'checkout.html')