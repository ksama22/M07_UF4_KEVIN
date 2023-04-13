from django.forms import ModelForm
from .models import Student, Teacher

#Es crea un formulari segons el OBJ 'Student'
class StudentForm(ModelForm):
    class Meta:
        model = Student
        #field = Student -> name, age
        fields = '__all__'

#Es crea un formulari segons el OBJ 'Teacher'
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        #field = Teacher -> name, course
        fields = '__all__'