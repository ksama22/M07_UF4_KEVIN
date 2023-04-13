from django.db import models
# Create your models here.

#Creado Teacher model for migrate
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=100)


#Creado Student model for migrate
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.CharField(max_length=100)

## Despres de canviar
# python .\jaumebalmes_kevin\manage.py makemigrations
# python .\jaumebalmes_kevin\manage.py migrate