from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template


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
    return HttpResponse(t.render({},request))

