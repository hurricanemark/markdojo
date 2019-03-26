from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
	return HttpResponse('Hey there.  Welcome to Mark dojo!')
