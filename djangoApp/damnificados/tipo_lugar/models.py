from django.db import models

from django.db import models

TIPO_LUGAR = (('H','Hospital'), ('C','Centro_Acopio'), ('E','Escuela'),('O','Otro'))

class Tipo_lugares(models.Model):
    tipo_lugar = models.CharField(choices = TIPO_LUGAR, max_length = 5)
# Create your models here.
