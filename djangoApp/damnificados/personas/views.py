# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Personas
from .serializer import PersonasGet, PersonasCreateSerializer
import json, requests
# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        gente = Personas.objects.all()
        serializer = PersonasGet(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        person=PersonasCreateSerializer(data=request.data)
        if person.is_valid():
            person.save()
            # self._sendPushNotification("Nueva Persona Creada","fLDxqyKHKDY:APA91bHvBxHsabs2K002i0WQ7SReARR_7X_OEv1GTC8V_wFPXK1nl08wuSfIE2Zudjdmc8wFrDkFdZ8KatLzvlSAAGyxZJ5IGfO8swi8vo0PIYB_z6UwreAD1L9C-MZNt5bNECL_kJGI")
            return Response(person.data,status=status.HTTP_201_CREATED)
        else:
            return Response(person, status=status.HTTP_400_BAD_REQUEST)

    def _sendPushNotification(self, msg, token):
        baseUrl = "https://fcm.googleapis.com/fcm/send"
        headers = {"Authorization":"key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY", "Content-Type":"application/json"}
        data = { "notification": {"title": "Sadot EscoBBBBBBBBBar","body": "5 to 1","icon": "firebase-logo.png","click_action": "http://localhost:8081"},"to" : token}
        data = json.dumps(data)
        pushNotification = requests.post(baseUrl, headers=headers, data=data)
        pushNotificationJson = pushNotification.json()
        if pushNotification.status_code == 200 and "error" not in pushNotificationJson['results'][0]:
            return True
        else:
            return False


class PersonaApi(APIView):

    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasGet(persona)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializers = PersonasGet(persona, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializers, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
