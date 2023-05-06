from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = ("Hola querido usuario")
    pagina_html = HttpResponse(saludo)
    return pagina_html
    
def saludar_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html