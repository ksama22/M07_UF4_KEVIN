from django.urls import path

from. import views

#Creada per conectar amb views.py
urlpatterns =[
    path('', views.index,name='index'),
    path('students', views.students,name='students'),
    path('teachers', views.teachers,name='teachers'),
    path('student/<str:pk>/', views.student ,name='student'),
    path('teacher/<str:pk>/', views.teacher ,name='teacher')

]