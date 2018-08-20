# -*- coding: utf-8 -*-

import os

import environ

ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(ROOT_DIR.path('.env').__str__())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#b68qv#(v-g26k3qt_-1ufg-prvsw2p)7@ctea*n!36-w23bv1'
SECRET_KEY = env('DJANGO_SECRET_KEY', default=SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', default=True)

SITE_ID = 1

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    # 'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'config', 'fixtures'),
    # ROOT_DIR.path('config/fixtures').__str__(),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# LANGUAGE_CODE = 'zh-hans'
LANGUAGE_CODE = env('DJANGO_LANGUAGE_CODE', default='zh-hans')

# TIME_ZONE = 'UTC'
TIME_ZONE = env('DJANGO_TIME_ZONE', default='UTC')

# USE_I18N = True
USE_I18N = env('DJANGO_USE_I18N', default=True)

# USE_L10N = True
USE_L10N = env('DJANGO_USE_L10N', default=True)

# USE_TZ = True
USE_TZ = env('DJANGO_USE_TZ', default=True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
