from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.template import loader
from personas.models import Persona


def bienvenida(request):
    pagina = loader.get_template('saludo.html')
    return HttpResponse(pagina.render( ))

def hola(request, nombre):
    apellido = request.GET["apellido"]
    nivel = request.GET["nivel"]
    curso = request.GET["curso"]
    nombreCompleto = nombre + " " + apellido
    pagina = loader.get_template('saludo.html')
    mensaje = {'nombre': nombreCompleto, 'curso':curso, 'nivel':nivel}
    return HttpResponse(pagina.render(mensaje))

def edad(request, edad):
    pagina = loader.get_template('edad.html')
    mensaje = {'edad': edad}
    return HttpResponse(pagina.render(mensaje))

def mostrar_personas(request):
    cantidad_personas = Persona.objects.count()
    personas = Persona.objects.all().values()
    nombres_personas = list
    datos = {'cantidad': cantidad_personas, 'personas': personas, 'nombres_personas':nombres_personas}
    pagina = loader.get_template('personas.html')
    return HttpResponse(pagina.render(datos, request))
    