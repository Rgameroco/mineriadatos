from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.template.loader import get_template
from .models import *
import random
def index(request):
    t = get_template('index.html')
    html = t.render({},request)
    return HttpResponse(html)

def sensorhumedad(request):
    t = get_template('datossensor.html')
    html = t.render({},request)
    return HttpResponse(html)
def tipoconstruccion(request):
    t = get_template('tipoconstruccion.html')
    html = t.render({},request)
    return HttpResponse(html)
def variables(request):
    t = get_template('variables.html')
    html = t.render({},request)
    return HttpResponse(html)
def principal(request):
    t = get_template('principal.html')
    lecturas = lecturasensor.objects.filter(idpersonasensor=1)
    context = {
        'lectura': lecturas,
    }
    return HttpResponse(t.render(context,request))

def mostrarPerfil(request):
    t = get_template('mostrarPerfil.html')
    persona1 = persona.objects.filter(id=5)
    context = {
        'persona1': persona1,
    }
    print(context)
    return  HttpResponse(t.render(context,request))
def prediccion(request):
    t = get_template('prediccion.html')
    humedad = random.randint(17,22)
    temperatura = random.randint(18,22)
    context = {
        'humedad':humedad,
        'temperatura':temperatura
    }
    html = t.render(context,request)
    return HttpResponse(html)