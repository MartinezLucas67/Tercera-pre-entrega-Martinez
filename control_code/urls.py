"""
URL configuration for proj_code project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('lista-cursos/', views.listar_cursos, name="lista_cursos"),
    path('crear-curso/', views.crear_curso, name="crear_curso"),
    path('buscar-cursos/', views.buscar_cursos, name="buscar_cursos"),
    path('eliminar-curso/<int:id>/', views.eliminar_curso, name="eliminar_curso"),
    path('editar-curso/<int:id>/', views.editar_curso, name="editar_curso"),
   
##Estudiantes
    path('estudiantes/', views.EstudianteListView.as_view(), name="lista_estudiantes"),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', views.EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', views.EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', views.EstudianteDeleteView.as_view(), name="eliminar_estudiante"),

##Profes
    path('profesores/', views.ProfesorListView.as_view(), name="lista_profesores"),
    path('ver-profesores/<int:pk>/', views.ProfesorDetailView.as_view(), name="ver_profesores"),
    path('buscar-profe/', views.buscar_profe, name="buscar_profe"),
    path('buscar/', views.BuscarProfesorView.as_view(), name='buscar_profesor'),
]