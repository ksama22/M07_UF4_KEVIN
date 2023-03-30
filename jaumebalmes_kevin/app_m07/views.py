from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.


#Fem referencia 'jaumebalmes_kevin\app_m07\urls.py'
#Carrega les dades al html indicat
def index(request):
    profe = {"name":"Roger","surname":"Sobrino","age":"17"}
    #Carrega el template de 'jaumebalmes_kevin\jaumebalmes_kevin\templates\head\index.html''
    template = loader.get_template('index.html')
    dades = template.render({"name":profe["name"],"surname":profe["surname"], "age":profe["age"]})
    return HttpResponse(dades)

#Carrega una paraula en concret
#def index(request):
#    return HttpResponse("Hola?")

#Carrega un index.html de 'jaumebalmes_kevin\app_m07\templates\index.html'
#def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())