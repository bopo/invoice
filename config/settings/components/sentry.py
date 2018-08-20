# -*- coding: utf-8 -*-

INSTALLED_APPS += ['raven.contrib.django.raven_compat', ]
RAVEN_CONFIG = {'dsn': env('DJANGO_RAVEN_DSN', default=None), } if DEBUG else None
