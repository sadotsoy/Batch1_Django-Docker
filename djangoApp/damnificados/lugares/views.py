# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Lugares
from .serializer import LugaresGet,LugaresCreateSerializer

# Create your views here.

class LugaresApi(APIView):

    def get(self, request):
        gente = Lugares.objects.all()
        serializer = LugaresGet(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        place=LugaresCreateSerializer(data=request.data)
        if place.is_valid():
            place.save()
            return Response(place.data,status=status.HTTP_201_CREATED)
        else:
            return Response(place, status=status.HTTP_400_BAD_REQUEST)

class LugarApi(APIView):

    def _getLugar(self, pk):
        try:
            return Lugares.objects.get(pk=pk)
        except Lugares.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        lugar = self._getPersona(pk)
        serializer = LugaresGet(lugar)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        lugar = self._getLugar(pk)
        serializers = LugaresGet(lugar, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializers, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lugar = self._getLugar(pk)
        lugar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
