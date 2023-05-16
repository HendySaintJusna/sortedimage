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
import requests
import os.path
import json
import string
import random



#Login
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

#Register
def register_user(request):

	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)

			# messages.success(request, ("Registration successful!"))
			return redirect('/home')

	else:	
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {
		'form': form,
		})




#Sign out
def logout_user(request):
	logout(request)
	# messages.success(request, ("You were logged out!"))
	return redirect('/')


#Home sign in page
def home_view(request, *args, **kwargs):

	current_user = request.user
	userid = current_user.id
	count = RarImage.objects.filter(idowner=userid).count()
	
	response = render(request, "main.html", {'count' : count})	
	return response



#Welcome page
def welcome_view(request, *args, **kwargs):

	if request.user.is_authenticated:

		return redirect('/home')

	else:

		if request.COOKIES.get('yesguest') == None :

			rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
			guest_name = 'user' + rand

			response = render(request, "welcome.html")

			response.set_cookie('yesguest', guest_name,  path='/')
			
			return response

		else:
			response = render(request, "welcome.html")
			return response
	


#Uploading images
def file_upload_guest(request):


	if request.method == "POST":

		guest_number = request.COOKIES.get('yesguest')
		uploaded_file = request.FILES
		allSorted = Sort.x(request)
		namezip = Sort.uploadInFolderGuest(allSorted,request,guest_number)

		return redirect('/collection')

	else:

		return render(request, "welcome.html")



#Uploading images
def file_upload(request):

	current_user = request.user
	userid = current_user.id
	data = RarImage.objects.all().filter(idowner=userid)
	count = 0

	for x in data:
		count = count + ((x.sizeinoctet)/1000000)


	if request.method == "POST":

		if count < 201:

			uploaded_file = request.FILES
			allSorted = Sort.x(request)
			namezip = Sort.uploadInFolder(allSorted,request)

			# messages.success(request, ("Your image is now organized by similarity. Check it out in the collection tab!"))
			return redirect('/collection')

		else:

			# messages.success(request, ("You have reach the maximum of uploaded Album (5)"))
			return redirect('/home')

	else:

		return render(request, "main.html")


	
#Display user sorted images collection
def collection_view(request):

	current_user = request.user
	userid = current_user.id
	data = RarImage.objects.filter(idowner=userid).order_by('-id')
	allmyrow = RarImage.objects.all().filter(idowner=userid)
	count = 0

	for x in allmyrow:
		count = count + ((x.sizeinoctet)/1000000)

	remain = round((200 - count), 2)
	return render(request, "collection.html", {'data':data, 'remain' : remain})


#Display a choisen sorted album
def ablumshare_view(request,str):
	album = RarImage.objects.filter(token=str)
	# album = get_object_or_404(RarImage, token=str)
	return render(request, 'album.html', {'data': album})

#Display a choisen sorted album
def ablumshare_viewguest(request):
	guest = request.COOKIES.get('yesguest')
	album = RarImage.objects.filter(guest=guest).last()
	# album = get_object_or_404(RarImage, token=str)
	return render(request, 'guestalbum.html', {'data': album})


def confid(request):
	return render(request, 'confidentiality.html')
