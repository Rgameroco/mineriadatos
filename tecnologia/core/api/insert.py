from django.http import HttpResponse
from django.views import View
from core.models import persona,rol,sensorhumedad
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

now = datetime.datetime.now()
@csrf_exempt
def guardarDatos(request):
        print('entro aqui')
        #print('holi c:',request.GET['nombre'])
        nombre = request.POST.get('nombre','')
        print("nombre : ",nombre)
        apellido = request.POST.get('apellido','')
        dni = request.POST.get('dni','')
        contrasenha = request.POST.get('contrasenha','')
        idrol =  rol.objects.get(pk = 1)
        p = persona(idrol = idrol,nombre_persona=nombre,apellido_persona = apellido, dni =dni,
                    contrasenha = contrasenha)
        p.save()
        return HttpResponse(request)
@csrf_exempt
def guardarSensor(request):
    print('entra')
    modelo = request.POST.get('modelo','')
    tipomedida = request.POST.get('tipomedida','')
    margenerror = float(request.POST.get('margenerror',''))
    fechacompra = now
    print(float(margenerror))
    temp = sensorhumedad(modelo = modelo,tipomedida=tipomedida,margenerrror=margenerror,fechacompra=fechacompra)
    temp.save()
    return HttpResponse('Enviado exitoso')