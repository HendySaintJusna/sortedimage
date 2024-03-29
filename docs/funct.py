from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from difflib import SequenceMatcher
from PIL import Image
from docs.models import RarImage 
import os.path
import imgcompare
import io
import string
import random
import shutil
import socket


from django.http import FileResponse
# Create your models here.

class Sort():

	

	@classmethod
	def openImg(cls,r):
		return Image.open(r)



	# Sort image by similarity
	@classmethod
	def x(cls,arrfile):

		array = []
		new_array = []
		remove_from_list = []
		results = []
		package = []
		final_list = []
		limit = 15


		if arrfile.method == 'POST':
			files = arrfile.FILES



			for z in files:
				array.append(files[z])

			count = len(array)
			new_array = array

			while count != 0:



				#restart
				target = new_array[0]

				
				for t in new_array:

					#percentage difference - maximum 20%
					perc = cls.checkSim(target,t)

					if perc < limit:

						if perc != 0:

							if len(remove_from_list) > 0:

								if t not in remove_from_list:
									package.append(t)
									remove_from_list.append(t)

							else:
								package.append(t)
								remove_from_list.append(t)

						else:

							if t not in remove_from_list:
								package.append(t)
								remove_from_list.append(t)
							

				#clean for restart
				results.append(list(package))
				package.clear()
				del new_array[0]
				count = len(new_array)


			#remove empty array
			for index,z in enumerate(results):
				if len(z) != 0:
					final_list.append(z)


			return final_list
			
			
	


	#percentage similarity calculator
	@classmethod
	def checkSim(cls,decoy,target):



		i1 = (Image.open(decoy).resize((50,50))).convert('RGB')
		i2 = (Image.open(target).resize((50,50))).convert('RGB')

	
		percentage = imgcompare.image_diff_percent(i1, i2)


		return percentage


	@classmethod
	def setIp(cls):
		return socket.gethostbyname(socket.gethostname())

	@classmethod
	def downloadImg(cls):
		return socket.gethostbyname(socket.gethostname())


	#Uploal all images in folders and zip it
	@classmethod
	def uploadInFolder(cls,arraySorted,request):

		arr = arraySorted
		count = 0

		letters = string.ascii_lowercase
		main_folder = ''.join(random.choice(letters) for i in range(5))


		while count != len(arr):
			
			arr = arraySorted

			letters = string.ascii_lowercase
			rand = 'category_' + str(count)
			

			namezip = 'Album_' + main_folder


			parent_dir = main_folder + '/' + rand
			 
			for img in arr[count]:

				name = img.name

				path = os.path.join(parent_dir, name)

				fs = FileSystemStorage()
				fs.save(path,img)
	

			count += 1

		current_user = request.user
		myid = current_user.id
		for_database_token = namezip + '.zip'
		

		# change directory
		os.chdir("C:/Users/Hendy/Desktop/imgsort/media")
		shutil.make_archive(namezip,'zip',main_folder)

		sizeko = (os.path.getsize(for_database_token))/1000

		if sizeko <= 999:
			sizeko = str(round((sizeko/1000), 2)) + ' MB'
		elif sizeko >= 1000 and sizeko <= 999999:
			convertmb = sizeko/1000
			sizeko = str(round(convertmb, 2)) + ' MB'
		elif sizeko >= 1000000 and sizeko <= 1000000000:
			convertgb = sizeko/1000000
			sizeko = str(round(convertgb, 2)) + ' GB'


		myData = RarImage(idowner=myid,name=main_folder, token=main_folder, file=for_database_token, size=sizeko, sizeinoctet=os.path.getsize(for_database_token))
		myData.save()


		return namezip
		




	#Uploal all images in folders and zip it
	@classmethod
	def uploadInFolderGuest(cls,arraySorted,request,guest_number):
		
		arr = arraySorted
		count = 0

		letters = string.ascii_lowercase
		main_folder = ''.join(random.choice(letters) for i in range(5))


		while count != len(arr):
			
			arr = arraySorted

			letters = string.ascii_lowercase
			rand = 'category_' + str(count)
			

			namezip = 'Album_' + main_folder


			parent_dir = main_folder + '/' + rand
			 
			for img in arr[count]:

				name = img.name

				path = os.path.join(parent_dir, name)

				fs = FileSystemStorage()
				fs.save(path,img)
	

			count += 1

		current_user = request.user
		myid = 0
		for_database_token = namezip + '.zip'
		

		# change directory
		os.chdir("C:/Users/Hendy/Desktop/imgsort/media")
		shutil.make_archive(namezip,'zip',main_folder)

		sizeko = (os.path.getsize(for_database_token))/1000

		if sizeko <= 999:
			sizeko = str(round((sizeko/1000), 2)) + ' MB'
		elif sizeko >= 1000 and sizeko <= 999999:
			convertmb = sizeko/1000
			sizeko = str(round(convertmb, 2)) + ' MB'
		elif sizeko >= 1000000 and sizeko <= 1000000000:
			convertgb = sizeko/1000000
			sizeko = str(round(convertgb, 2)) + ' GB'



		myData = RarImage(idowner=myid,name=main_folder, token=main_folder, file=for_database_token, size=sizeko, sizeinoctet=os.path.getsize(for_database_token), guest=guest_number)
		myData.save()


		return namezip


