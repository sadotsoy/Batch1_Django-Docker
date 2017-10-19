# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lugares
from .serializer import *

import json

class LugaresTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.first_lugar = Lugares.objects.create(
            nombre="Hospital",
            calle = "Tizoc 123",
            codigo_postal = 45
        )
        self.second_lugar = Lugares.objects.create(
            nombre="Escuela",
            calle = "Moctezuma 451",
            codigo_postal = 44215
        )
        self.lugar_correct_json = {
            "nombre": "Pqeqw",
            "calle": "pqeqeqe",
            "codigo_postal": 45
        }
        self.lugar_incorrect_json = {
            "nombre": "Pqeqw",
            "calle": 4124,
            "codigo_postal": 45
        }
        def test_get_all_lugares(self):
            response = self.client.get(reverse('lugares_endpoint'))
            lugares = Lugares.objects.all()
            serializer = LugaresGet(lugares, many=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(serializer.data, response.data)

        def test_get_one_lugar(self):
            response = self.client.get(reverse('lugar_endpoint',kwargs={'pk':self.first_lugar.id}))
            lugar = Lugares.objects.get(pk=self.first_lugar.id)
            serializer = LugaresGet(lugar)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(serializers.data, response.data)

        def test_post_lugar(self):
            response = self.client.post(reverse('lugares_endpoint'),data = json.dumps(self.lugar_correct_json),content_type="application/json")
            self.assertEqual(response.status_code, 201)

        def test_delete_lugar(self):
            response = self.client.delete(reverse('lugar_endpoint',kwargs={'pk': self.second_lugar.id}))
            self.assertEqual(response.status_code, 204)

        def test_put_lugar(self):
            response = self.client.put(reverse('lugar_endpoint',
                                               kwargs={'pk':self.first_lugar.id}),
                                       data=json.dumps(self.lugar_correct_json),
                                       content_type="application/js")
            self.assertEqual(response.status_code,202)
