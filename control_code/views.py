from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Estudiante, Curso, Profesor
from .forms import EstudianteForm, CursoForm, ProfesorForm




def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all()
    }
    http_response = render(
        request=request,
        template_name='control_code/lista_cursos.html',
        context=contexto,
    )
    return http_response

def registrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'registrar_curso.html', {'form': form})

def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data  
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(nombre=nombre, comision=comision)  
            curso.save()
            url_exitosa = reverse('lista_cursos') 
            return redirect(url_exitosa)
    else: 
        form = CursoForm()
    http_response = render(
        request=request,
        template_name='control_code/form_curso.html',
        context={'form': form}
    )
    return http_response

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda)
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_code/lista_cursos.html',
            context=contexto,
        )
        return http_response

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        form = CursoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:  
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
        }
        form = CursoForm(initial=inicial)
    return render(
        request=request,
        template_name='control_code/form_curso.html',
        context={'form': form},
    )


##########EJEMPLO CLASEE######
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'control_code/lista_estudiantes.html'

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ('nombre', 'apellido', 'email', 'dni', 'telefono')
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteDetailView(DetailView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni', 'telefono')
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')


##Ejemplo clase pero con profe
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'control_code/lista_profesor.html'
class ProfesorDetailView(DetailView):
    model = Profesor
    success_url = reverse_lazy('lista_profesor')

def buscar_profe(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        profesores = Profesor.objects.filter(apellido__contains=busqueda)
        contexto = {
            "profesores": profesores,
        }
        http_response = render(
            request=request,
            template_name='control_code/lista_profesor.html',
            context=contexto,
        )
        return http_response
    
class BuscarProfesorView(ListView):
    model = Profesor
    template_name = 'control_code/lista_profesor.html'
    context_object_name = 'profesores'

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Profesor.objects.filter(nombre__icontains=busqueda)
        else:
            return Profesor.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda')
        return context