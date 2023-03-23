from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
#Fem referencia al urls.py
def index(request):
    profe = {"name":"Roger","surname":"Sobrino","age":"17"}
    #Carrega el template de 'jaumebalmes_kevin\jaumebalmes_kevin\templates\head\index.html''
    template = loader.get_template('index.html')
    dades = template.render({"name":profe["name"],"surname":profe["surname"], "age":profe["age"]})
    return HttpResponse(template.render(dades))