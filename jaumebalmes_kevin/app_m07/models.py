from django.db import models
# Create your models here.

#Creado Teacher model for migrate
class Teacher(models.Model):
    name = models.CharField
    course = models.CharField

#Creado Student model for migrate
class Student(models.Model):
    name = models.CharField
    age = models.IntegerField

## Despres de canviar
# python .\jaumebalmes_kevin\manage.py makemigrations
# python .\jaumebalmes_kevin\manage.py migrate