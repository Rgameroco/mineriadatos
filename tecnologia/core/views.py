from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template


def index(request):
    t = get_template('index.html')
    html = t.render({},request)
    return HttpResponse(html)

