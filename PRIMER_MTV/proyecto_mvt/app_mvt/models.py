from django.db import models

# Create your models here.

class Familia (models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    relacion = models.CharField(max_length=40)
    fecha_nac = models.DateField ()
