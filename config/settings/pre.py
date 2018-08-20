# -*- coding: utf-8 -*-
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE
from split_settings.tools import include

include(
    'components/base.py',
    'components/apps.py',
    'components/suit.py',
    'components/const.py',
    'components/static.py',
)

DEBUG = env('DJANGO_DEBUG', default=False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME', default='subway'),
        'USER': env('POSTGRES_USER', default='subway'),
        'PASSWORD': env('POSTGRES_PASS', default='subway'),
        'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env('POSTGRES_PORT', default='5432'),
        'OPTIONS': {
            'isolation_level': ISOLATION_LEVEL_SERIALIZABLE,
            'client_encoding': 'UTF8',
        },
        'timezone': 'UTC',
    }
}
