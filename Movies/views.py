from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
import MyDB

# Create your views here. unitted import loader to check

def index(request):
    movie= get_code(movie)
    released= get_code(released)
    diccionario = {'mov':movie, 'year': released}
    # plantilla = loader.get_template('template1.html')
    # documento = plantilla.render(diccionario)
    diccionario()
    return HttpResponse (diccionario)