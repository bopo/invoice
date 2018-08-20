# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status

from .common import BaseAPITestCase

import pytest

from django.db import connection
from django.conf import settings

original_db_name = settings.DATABASES["default"]["NAME"]

@pytest.mark.django_db
class TestAppFeedbackCase(BaseAPITestCase):
    def setUp(self):
        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    @pytest.fixture(autouse=True)
    def setup_stuff(self, db):
        Question.objects.create(question_text="How are you?")

    @pytest.fixture(autouse=True)  
    def setup_method(self, method):
        assert connection.settings_dict["NAME"] == settings.DATABASES["default"]["NAME"]

    def test_feedback_commit(self):
        data = {
            "title": "test",
            "content": "content",
            "phone": "12312312"
        }
        response = self.client.post("/api/feedback/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_feedback_list(self):
        response = self.client.get("/api/feedback/")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
