from django.conf.urls import url
from core.views import index,sensorhumedad,tipoconstruccion,variables,principal
from core.api import insert
from django.urls import path

app_name = 'core'
urlpatterns= [
    url(r'^index/$', index,name='index'),
    url(r'^sensorhumedad/$',sensorhumedad,name='sensorhumedad'),
    url(r'^tipoconstruccion/$',tipoconstruccion,name='tipoconstruccion'),
    url(r'^variables/$',variables,name='variables'),
    url(r'^principal/$',principal,name='principal'),
    url(r'^$',principal,name='principal'),

    path('personaint/',insert.guardarDatos,name='insert_persona'),
    path('sensornew/',insert.guardarSensor,name='insert_sensor')
]

