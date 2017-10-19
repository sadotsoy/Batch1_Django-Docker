# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Personas
from .serializer import *

import json

class PersonasTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.first_persona = Personas.objects.create(
            nombre="Ludoviko",
            edad = 40,
            sexo = "H",
            tipo_de_personas = "Voluntario"
        )
        self.second_persona = Personas.objects.create(
            nombre="Federica",
            edad = 36,
            sexo = "I",
            tipo_de_personas = "Voluntario"
        )
        self.persona_correcta_json = {
            "nombre": "NecesitoComerAlgo@!plis",
            "edad" : 33,
            "sexo": "M",
            "tipo_de_personas": "Voluntario"
        }
        self.persona_incorrecta_json = {
            "nombre": "NecesitoComerAlgo@!plis",
            "edad" : 33,
            "sexo": 666,
            "tipo_de_personas": "Voluntario"
        }
    def test_get_all_personas(self):
        response = self.client.get(reverse('personas_endpoint'))
        personas = Personas.objects.all()
        serializer = PersonasGet(personas, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_one_persona(self):
        response = self.client.get(reverse('persona_endpoint',kwargs={'pk': self.first_persona.id}))
        persona = Personas.objects.get(pk=self.first_persona.id)
        serializer = PersonasGet(persona)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_post_persona(self):
        response = self.client.post(reverse('personas_endpoint'),data = json.dumps(self.persona_correcta_json),content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_delete_persona(self):
        response = self.client.delete(reverse('persona_endpoint',kwargs={'pk':self.second_persona.id}))
        self.assertEqual(response.status_code, 204)

    def test_put_persona(self):
        response = self.client.put(reverse('persona_endpoint',
                                              kwargs={'pk':self.first_persona.id}),
                                              data=json.dumps(self.persona_correcta_json),
                                              content_type="application/json")
        self.assertEqual(response.status_code,202)
