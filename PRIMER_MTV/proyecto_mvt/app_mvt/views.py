from django.shortcuts import render
from app_mvt.models import Familia
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.


def familia (request):
    familia = Familia.objects.all()
    datos = {"familia": familia}
    plantilla = loader.get_template("plantilla.html")
    documento = plantilla.render (datos)
    return HttpResponse (documento)

def ingreso_flia (request, nombre, edad, relacion, fecha_nac):
    familia = Familia(nombre=nombre, apellido="Pradal", edad =edad, relacion=relacion, fecha_nac=fecha_nac)
    familia.save()
    texto = f"Se guardo en la BD el integrante {familia.relacion}, nombre {familia.nombre}"
    return HttpResponse (texto)