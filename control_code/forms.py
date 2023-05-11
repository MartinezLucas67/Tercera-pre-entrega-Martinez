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


'''class BuscarForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    opciones = (
        ('estudiantes', 'Estudiantes'),
        ('cursos', 'Cursos'),
        ('profesores', 'Profesores'),
    )
    categoria = forms.ChoiceField(choices=opciones) '''

