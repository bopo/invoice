# -*- coding: utf-8 -*-

ANONYMOUS_USER_ID = -1

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTH_USER_MODEL = 'consumer.CustomUser'
# AUTH_PROFILE_MODULE = 'consumer.Profile'

# EMAIL_HOST = env("DJANGO_EMAIL_HOST", default="")
# EMAIL_PORT = env("DJANGO_EMAIL_PORT", default=25)
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_USE_TLS = env("DJANGO_EMAIL_NAME", default=False)
# EMAIL_HOST_NAME = env("DJANGO_EMAIL_NAME", default="")
# EMAIL_HOST_USER = env("DJANGO_EMAIL_USER", default="")
# EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_PASS", default="")

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'service.restauth.backends.CustomUserBackend',
# )

# ACCOUNT_AUTHENTICATION_METHOD = 'mobile'

INSTALLED_APPS += (

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.github',

)

SOCIALACCOUNT_PROVIDERS = {
    'weixin': {
        'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize',  # for media platform
        'SCOPE': ['snsapi_base'],
    }
}

SITE_ID = 1
