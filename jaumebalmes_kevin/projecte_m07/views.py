from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Fem referencia al urls.py
def index(request):
    return HttpResponse("Error418, dame cafe")