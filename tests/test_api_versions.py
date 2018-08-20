# -*- coding: utf-8 -*-
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestAppVersion(APITestCase):
    def test_version_list(self):
        response = self.client.get('/api/versions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK,response.json())
