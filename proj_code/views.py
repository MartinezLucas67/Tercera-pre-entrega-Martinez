from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_code/index.html',
        context=contexto,
    )
    return http_response