from django.db import models
# Create your models here.

#Creado Teacher model for migrate
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)


#Creado Student model for migrate
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

## Despres de canviar
# python .\jaumebalmes_kevin\manage.py makemigrations
# python .\jaumebalmes_kevin\manage.py migrate