# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status

from .common import BaseAPITestCase


class TestAppFollowCase(BaseAPITestCase):
    def setUp(self):
        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_follow_list(self):
        response = self.client.get("/api/me/follow/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
