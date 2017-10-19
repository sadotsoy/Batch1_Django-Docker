# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# from personas.models import Personas
# Create your models here.

STATUS = (('1','Actual'),('0','Ya no'))

class Lugares(models.Model) :
    nombre = models.CharField(max_length = 180)
    calle = models.CharField(max_length = 100)
    colonia = models.CharField(max_length = 100)
    # tipo_lugar = models.ForeingKey(models.Tipo_lugares)
    # numero = models.CharField(max_length = 5)
    # estado = models.CharField(max_length = 50)
    # municipio = models.CharField(max_length = 50)
    # coordenadas = models.CharField(max_length = 50)
    codigo_postal = models.IntegerField(max_length = 6)
    #Geolocation Needed?

# class PersonasHasLugares(models.Model):
#     fecha = models.DateField()
#     status = models.CharField(choices=STATUS, max_length = 20)
#     lugares_id = models.ForeignKey(Lugares)
#     personas_id = models.ForeignKey(Personas)
