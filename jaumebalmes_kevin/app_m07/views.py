from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .forms import StudentForm, TeacherForm
from .models import Teacher, Student
# Create your views here.
#Fem referencia 'jaumebalmes_kevin\app_m07\urls.py'
#Carrega les dades al html indicat
#def index(request):
#    profe = {"name":"Roger","surname":"Sobrino","age":"17"}
#    #Carrega el template de 'jaumebalmes_kevin\jaumebalmes_kevin\templates\head\index.html''
#    template = loader.get_template('index.html')
#    dades = template.render({"name":profe["name"],"surname":profe["surname"], "age":profe["age"]})
#    return HttpResponse(dades)

#Carrega una paraula en concret
#def index(request):
#    return HttpResponse("Hola?")

#Carrega un index.html de 'jaumebalmes_kevin\app_m07\templates\index.html'
def index(request):
     template = loader.get_template('index.html')
     return HttpResponse(template.render())

def users(request):
    a = True
    context = {'a':a}
    return render(request, 'users.html',context)

#Carrega tots els profesors
def teachers(request):
    #Agafa tots de la base de dades
    teacherBBDDList = Teacher.objects.all()
    context = {'tchrs':teacherBBDDList}
    #context = {"tchrs": teachersList}
    return render(request, 'teachers.html', context)

#Carrega tots els estudiants
def students(request):
    #Agafa tots de la base de dades
    studentBBDDList = Student.objects.all()
    context = {"stdnts": studentBBDDList}
    return render(request, 'students.html',context)

#Carrega un estudiant
def student(request, pk):
    #La trucada la fa per una 'id' en concreta
    student_obj = Student.objects.get(id=pk)
    return render(request, 'student.html',{'stdnt':student_obj})

#Carrega un profesor
def teacher(request, pk):
     #La trucada la fa per una 'id' en concreta
     teacher_obj = Teacher.objects.get(id=pk)
     return render(request, 'teacher.html',{'tchr':teacher_obj})

#Formulari Student
def student_form(request):
    form = StudentForm(request.POST)
    if request.method == 'POST':
        #Si es un metode post i el valid, envia el formulari
        if form.is_valid():
            #Si es valid l'envia
            form.save()
            # redirecciona a la 'url' /students
            return redirect('students')
    context = {'forms':form}
    return render(request,'form.html',context)

#Formulari Teacher
def teacher_form(request):
    form = TeacherForm(request.POST)
    if request.method == 'POST':
        #Si es un metode post i el valid, envia el formulari
        if form.is_valid():
            #Si es valid l'envia
            form.save()
            # redirecciona a la 'url' /teachers
            return redirect('teachers')
    context = {'forms':form}
    return render(request,'form.html',context)

#Formulari Update student
def update_student(request, pk):
    #Agafa les dades del 'student' en concret
    student = Student.objects.get(id = pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        # redirecciona a la 'url' /students
        return redirect('students')
    context = {'forms':form}
    return render(request,'form.html',context)

#Formulari Update teacher
def update_teacher(request, pk):
    #Agafa les dades del 'teacher' en concret
    teacher = Teacher.objects.get(id = pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        # redirecciona a la 'url' /teachers
        return redirect('teachers')
    context = {'forms':form}
    return render(request,'form.html',context)

#Defineix dos llistes per defecte de les dades
teachersList = [  {"id": 1,"name": "Pedro Perez","course": "Matematicas"  },  {"id": 2,"name": "Maria Garcia","course": "Historia"  },  {"id": 3,"name": "Pedro Gomez","course": "Ciencias"  },  {"id": 4,"name": "Ana Lopez","course": "Literatura"  },  {"id": 5,"name": "Carlos Sanchez","course": "Ingles"  },  {"id": 6,"name": "Laura Torres","course": "Educacion Fisica"  },  {"id": 7,"name": "Javier Hernandez","course": "Filosofia"  },  {"id": 8,"name": "Silvia Ruiz","course": "Quimica"  },  {"id": 9,"name": "Antonio Martinez","course": "Geografia"  },  {"id": 10,"name": "Isabel Torres","course": "Arte"  }]
studentList = [  {"id": 1,"name": "Juan Garcia","age": 17  },  {"id": 2,"name": "Maria Lopez","age": 18  },  {"id": 3,"name": "Pedro Gomez","age": 16  },  {"id": 4,"name": "Ana Ruiz","age": 17  },  {"id": 5,"name": "Carlos Sanchez","age": 18  },  {"id": 6,"name": "Laura Torres","age": 16  },  {"id": 7,"name": "Javier Hernandez","age": 17  },  {"id": 8,"name": "Silvia Flores","age": 16  },  {"id": 9,"name": "Antonio Martinez","age": 18  },  {"id": 10,"name": "Isabel Torres","age": 17  }]
