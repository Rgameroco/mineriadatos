from django.http import HttpResponse
from django.views import View
from core.models import persona,rol,sensorhumedad
from django.views.decorators.csrf import csrf_exempt
import json
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

def guardarSensor(request):
    print('entra')
    modelo = request.POST.get('modelo','')
    tipomedida = request.POST.get('tipomedida','')
    margenerror = request.POST.get('margenerror','')
    fechacompra = request.POST.get('fechacompra','')
    print(type(margenerror))
    temp = sensorhumedad(modelo = modelo,tipomedida=tipomedida,margenerror=margenerror,fechacompra=fechacompra)
    temp.save()
    return HttpResponse('Enviado exitoso')