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

def users(request):
    a = True
    context = {'a':a}
    return render(request, 'users.html',context)

def teachers(request):
    teachersList = [  {"id": 1,"name": "Juan Perez","course": "Matematicas"  },  {"id": 2,"name": "Maria Garcia","course": "Historia"  },  {"id": 3,"name": "Pedro Gomez","course": "Ciencias"  },  {"id": 4,"name": "Ana Lopez","course": "Literatura"  },  {"id": 5,"name": "Carlos Sanchez","course": "Ingles"  },  {"id": 6,"name": "Laura Torres","course": "Educacion Fisica"  },  {"id": 7,"name": "Javier Hernandez","course": "Filosofia"  },  {"id": 8,"name": "Silvia Ruiz","course": "Quimica"  },  {"id": 9,"name": "Antonio Martinez","course": "Geografia"  },  {"id": 10,"name": "Isabel Torres","course": "Arte"  }]
    context = {"tchrs": teachersList}
    return render(request, 'teachers.html', context)

def students(request):
    studentList = [  {"id": 1,"name": "Juan Garcia","age": 17  },  {"id": 2,"name": "Maria Lopez","age": 18  },  {"id": 3,"name": "Pedro Gomez","age": 16  },  {"id": 4,"name": "Ana Ruiz","age": 17  },  {"id": 5,"name": "Carlos Sanchez","age": 18  },  {"id": 6,"name": "Laura Torres","age": 16  },  {"id": 7,"name": "Javier Hernandez","age": 17  },  {"id": 8,"name": "Silvia Flores","age": 16  },  {"id": 9,"name": "Antonio Martinez","age": 18  },  {"id": 10,"name": "Isabel Torres","age": 17  }]
    context = {"stdnts": studentList}
    return render(request, 'students.html',context)
