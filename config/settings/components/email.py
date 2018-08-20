# -*- coding: utf-8 -*-

EMAIL_HOST = env("DJANGO_EMAIL_HOST", default="")
EMAIL_PORT = env("DJANGO_EMAIL_PORT", default=25)

EMAIL_HOST_NAME = env("DJANGO_EMAIL_NAME", default="")
EMAIL_HOST_USER = env("DJANGO_EMAIL_USER", default="")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_PASS", default="")

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
