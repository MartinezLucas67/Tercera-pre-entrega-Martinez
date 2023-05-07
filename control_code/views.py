from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Lucas", "apellido": "Martinez"}
        ]
    }
    http_response = render(
        request=request,
        template_name='control_code/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Python", "comision": "40440"},
            {"nombre": "Frontend", "comision": "10110"},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_code/lista_cursos.html',
        context=contexto,
    )
    return http_response
