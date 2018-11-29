from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(rol)
admin.site.register(persona)
admin.site.register(tipoentrada)
admin.site.register(tipoconstruccion)
admin.site.register(numeroentradas)
admin.site.register(variables)
admin.site.register(ambiente)
admin.site.register(sensorhumedad)
admin.site.register(persona_sensor)
admin.site.register(lecturasensor)