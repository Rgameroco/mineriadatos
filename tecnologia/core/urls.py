from django.conf.urls import url
from core.views import index,sensorhumedad,tipoconstruccion,variables
app_name = 'core'
urlpatterns= [
    url(r'^index/$', index,name='index'),
    url(r'^sensorhumedad/$',sensorhumedad,name='sensorhumedad'),
    url(r'^tipoconstruccion/$',tipoconstruccion,name='tipoconstruccion'),
    url(r'^variables/$',variables,name='variables'),
]

