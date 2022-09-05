from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def saludo(request):
    return HttpResponse("<h1>ejemplo app 2 vista1</h1>")




