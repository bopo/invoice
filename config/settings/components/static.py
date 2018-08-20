# -*- coding: utf-8 -*-

STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')
THUMB_ROOT = str(ROOT_DIR.path('assets/media/thumb'))
MEDIA_ROOT = str(ROOT_DIR.path('assets/media'))
MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')

if not DEBUG:
    STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(ROOT_DIR.path('assets/static')))
else:
    STATICFILES_DIRS = [
        str(ROOT_DIR.path('assets/static')),
    ]

ADMIN_MEDIA_PREFIX = MEDIA_URL
