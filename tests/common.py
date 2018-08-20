# -*- coding: utf-8 -*-
import json

from django.conf import settings
from django.utils.encoding import force_text
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):
    """
    base for API tests:
        * easy request calls, f.e.: self.post(url, data), self.get(url)
        * easy status check, f.e.: self.post(url, data, status_code=200)
    """

    def _generate_uid_and_token(self, user):

        result = {}

        self.token, _ = Token.objects.get_or_create(user=user)

        result['id'] = user.pk
        # result['uid'] = user.profile.uid
        result['token'] = self.token

        return result

    def send_request(self, request_method, *args, **kwargs):
        request_func = getattr(self.client, request_method)
        status_code = None

        if 'content_type' not in kwargs and request_method != 'get':
            kwargs['content_type'] = 'application/json'

        if 'data' in kwargs and request_method != 'get' and kwargs['content_type'] == 'application/json':
            data = kwargs.get('data', '')
            kwargs['data'] = json.dumps(data)  # , cls=CustomJSONEncoder

        if 'status_code' in kwargs:
            status_code = kwargs.pop('status_code')

        if hasattr(self, 'token'):
            kwargs['HTTP_AUTHORIZATION'] = 'Token %s' % self.token

        self.response = request_func(*args, **kwargs)

        is_json = bool([x for x in self.response._headers['content-type'] if 'json' in x])

        self.response.json = {}

        if is_json and self.response.content:
            self.response.json = json.loads(force_text(self.response.content))

        if status_code:
            self.assertEqual(self.response.status_code, status_code)

        return self.response

    def post(self, *args, **kwargs):
        return self.send_request('post', *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.send_request('get', *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.send_request('patch', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.send_request('put', *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.send_request('delete', *args, **kwargs)

    def init(self):
        settings.DEBUG = True

        # self.login_url = reverse('rest_login')
        # self.logout_url = reverse('rest_logout')

        # def _login(self):
        #     payload = {"username": self.USERNAME, "password": self.PASS}
        #     self.post(self.login_url, data=payload, status_code=status.HTTP_200_OK)
        #
        # def _logout(self):
        #     self.post(self.logout_url, status=status.HTTP_200_OK)
