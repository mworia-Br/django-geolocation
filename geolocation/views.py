from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def home(request):

   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

   if x_forwarded_for:

       ip = x_forwarded_for.split(',')[0]

   else:

       ip = request.META.get('REMOTE_ADDR')

  

   return HttpResponse("Welcome! You are visiting from: {}".format(ip))




api_key = '8a7257a890b34f7599bfd6f0049b0398';

api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


get_ip_geolocation_data(ip_address):


    response = requests.get(api_url + "&ip_address=" + ip_address)

    print(response.content)
    