# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEXOS =  (('M','Mujer'),('H','Hombre'),('I','Indefinido'))
TIPOS_PERSONAS= (('D','Damnificado'),('Voluntario','Voluntario'),('Otro','Otro'))
class Personas(models.Model) :
    nombre = models.CharField(max_length = 180)
    edad = models.IntegerField()
    sexo = models.CharField(choices= SEXOS, max_length = 5)
    tipo_de_personas = models.CharField(choices= TIPOS_PERSONAS, max_length=50)
