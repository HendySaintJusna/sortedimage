from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your models here.

class RarImage(models.Model):
	idowner = models.IntegerField(default=0)
	name = models.CharField(max_length=100)
	token = models.CharField(max_length=100)
	file = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)



