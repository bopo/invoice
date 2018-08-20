# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status

from .common import BaseAPITestCase


class TestAppProfileCase(BaseAPITestCase):

    def setUp(self):
        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_profile_commit(self):
        payloads = {
            "name": "121",
            "nick": "12",
            "mobile": "18500215943",
            "gender": "male",
            "birthday": "2018-07-25",
            "balance": "100.00",
        }

        response = self.client.put("/api/me/profile/", data=payloads)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_profile_show(self):
        response = self.client.get("/api/me/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_profile_avatar(self):
        response = self.client.get("/api/me/profile/avatar/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_profile_avatar_commit(self):
        payloads = {"avatar": open('assets/media/avatar/2.jpg', 'rb')}
        response = self.client.put("/api/me/profile/avatar/", data=payloads)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
