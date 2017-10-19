from rest_framework import serializers
from .models import Personas

SEXOS =  (('M','Mujer'),('H','Hombre'),('I','Indefinido'))
TIPOS_PERSONAS= (('D','Damnificado'),('Voluntario','Voluntario'),('Otro','Otro'))

def valida_edad(source):
    if source<= 100:
        pass
    else:
        raise serializers.ValidationError("Ay ajaaaaaaa, no seas mamoln!")

class PersonasGet(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['id','nombre','edad','sexo','tipo_de_personas']

class PersonasCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Personas
        fields = ['nombre','edad','sexo','tipo_de_personas']

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)
