from django import forms
from .models import Curso, Estudiante, Profesor

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'#['nombre', 'comision']

        

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'#['nombre', 'apellido', 'fecha_nacimiento', 'dni', 'telefono', 'email', 'biografia']
