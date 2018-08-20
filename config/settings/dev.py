# -*- coding: utf-8 -*-
from split_settings.tools import include, optional

include(
    'components/base.py',
    'components/apps.py',
    'components/suit.py',
    'components/const.py',
    'components/static.py',
    optional('components/debug.py'),
)

# DEBUG = env('DJANGO_DEBUG', default=True)
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}
