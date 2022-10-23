from django.shortcuts import render, HttpResponse

# Create your views here.

from django.shortcuts import render, HttpResponse

def home(request):

   return HttpResponse("Welcome!")