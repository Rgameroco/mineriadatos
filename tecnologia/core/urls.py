from django.conf.urls import url
from core.views import index
app_name = 'core'
urlpatterns= [
    url(r'^index/$', index,name='index'),
]

