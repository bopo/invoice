# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from .common import BaseAPITestCase


class TestApiPasssportCase(BaseAPITestCase):
    def setUp(self):
        owenr = get_user_model().objects.create_user(username='18500215940', email='ibopo@12.com', password='12312312',
                                                     is_active=True)
        self._generate_uid_and_token(user=owenr)

    def test_signin(self):
        data = {
            "username": "18500215940",
            "password": "12312312",
        }
        response = self.client.post(reverse('rest_signin'), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK, response.json())

    def test_signup(self):
        data = {
            "username": "18500215943",
            "password": "12312312",
            "verify": "1234",
        }
        response = self.client.post(reverse('rest_register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_passport_reset(self):
        data = {
            "username": "18500215940",
        }
        response = self.client.post(reverse('rest_password_reset'), data=data)

    def test_password_reset_confirm(self):
        data = {
            "username": "18500215940",
            "password": "12312312",
            "verify": "1234",
        }
        response = self.client.post(reverse('rest_password_reset_confirm'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_password_change(self):
        data = {
            "old_password": "12312312",
            "new_password1": "18500215943",
            "new_password2": "18500215943",
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        response = self.client.post(reverse('rest_password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_password_change_password_mismatch(self):
        data = {
            "old_password": "12312312",
            "new_password1": "18500215943",
            "new_password2": "1111",
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        response = self.client.post(reverse('rest_password_change'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())

    def test_passport_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

        response = self.client.get(reverse('rest_logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
