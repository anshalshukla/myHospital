from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from validate_email import validate_email
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User, Group
from profiles.models import Patient, Doctor

# Create your views here.
def register(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You already have a account and you are Logged in.')
		return HttpResponseRedirect('/home') 
	else:
		c = {}
		c.update(csrf(request))
		return render(request, 'loginmodule/register.html', c)

def login(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You are already Logged in.')
		return HttpResponseRedirect('/home')
	else:
		c = {}
		c.update(csrf(request))
		return render(request, 'loginmodule/login.html', c)

def register_view(request):
	firstname = request.POST.get('firstname', '')
	lastname = request.POST.get('lastname', '')
	username = request.POST.get('username', '')
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	confirmPassword = request.POST.get('confirm-password', '')
	registerAs = request.POST.get('register_as', '')

	if validate_email(email) is False:
		messages.add_message(request, messages.WARNING, 'Invalid Email!')
		return HttpResponseRedirect('/register')

	if password != confirmPassword:
		messages.add_message(request, messages.WARNING, 'Password does not match.')
		return HttpResponseRedirect('/register')
	
	if len(User.objects.filter(email=email)) != 0:
		messages.add_message(request, messages.WARNING, 'Email already registed.')
		return HttpResponseRedirect('/register')

	if len(User.objects.filter(username=username)) != 0:
		messages.add_message(request, messages.WARNING, 'Username taken!')
		return HttpResponseRedirect('/register')

	user = User(username=username, first_name=firstname, last_name=lastname, email=email)
	user.set_password(password)
	user.save()
	if registerAs == 'patient' or registerAs == 'doctor':
		group = Group.objects.get(name=registerAs)
		group.user_set.add(user)
	
	if registerAs == 'patient':
		Patient.objects.create(user=user)

	if registerAs == 'doctor':
		Doctor.objects.create(user=user)
		
	auth.login(request, user)
	messages.add_message(request, messages.INFO, 'Your are now Logged in.')
	return HttpResponseRedirect('/home')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		messages.add_message(request, messages.INFO, 'Your are now Logged in.')
		return HttpResponseRedirect('/home')
	else:
		messages.add_message(request, messages.WARNING, 'Invalid Login Credentials.')
		return HttpResponseRedirect('/login')

def logout(request):
	if request.user.is_authenticated:
		auth.logout(request)
	messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
	messages.add_message(request, messages.INFO, 'Thanks for visiting.')
	return HttpResponseRedirect('/login')
