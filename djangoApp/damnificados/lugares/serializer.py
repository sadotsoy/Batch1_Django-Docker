# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Lugares

class LugaresGet(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['nombre','calle','colonia','codigo_postal']

class LugaresCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Lugares
        fields = ['nombre','calle','colonia','codigo_postal']

class LugaresModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['nombre','calle','colonia','codigo_postal']
