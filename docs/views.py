from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterUserForm
from docs.models import RarImage 
from .funct import Sort
import os.path
import json
import string
import random




def login_user(request):
	
	if request.method == "POST":

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/home')

		else:
			messages.success(request, ("There Was An error login in, Try again..."))
			return redirect('/login')

	else:
		return render(request, 'authenticate/login.html', {})


def register_user(request):

	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration successful!"))
			return redirect('/home')

	else:	
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {
		'form': form,
		})





def logout_user(request):
	logout(request)
	messages.success(request, ("You were logged out!"))
	return redirect('/')


# Create your views here.
def home_view(request, *args, **kwargs):
	response = render(request, "main.html")
	return response

def welcome_view(request, *args, **kwargs):
	response = render(request, "welcome.html")
	return response


def file_upload(request):

	if request.method == "POST":

		uploaded_file = request.FILES
		allSorted = Sort.x(request)
		namezip = Sort.uploadInFolder(allSorted,request)

		# messages.success(request, ("Your image is now sorted by similarity and in a zip file. Check it out in the collection tab!"))
		return redirect('/collection')


	else:

		return render(request, "main.html")


	

def collection_view(request):

	current_user = request.user
	userid = current_user.id
	data = RarImage.objects.filter(idowner=userid).order_by('-id')
	return render(request, "collection.html", {'data':data})



def ablumshare_view(request,str):
	album = RarImage.objects.filter(token=str)
	# album = get_object_or_404(RarImage, token=str)
	return render(request, 'album.html', {'data': album})


def arr_view(request):
	return render(request, 'result.html', {'img': 'Mchien'})






		

