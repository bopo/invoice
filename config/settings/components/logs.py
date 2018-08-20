# -*- coding: utf-8 -*-

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#          'require_debug_false': {
#              '()': 'django.utils.log.RequireDebugFalse'
#          }
#      },
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(message)s'
#         },
#     },
#     'handlers': {
#         # Include the default Django email handler for errors
#         # This is what you'd get without configuring logging at all.
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false'],
#              # But the emails are plain text by default - HTML is nicer
#             'include_html': True,
#         },
#         # Log to a text file that can be rotated by logrotate
#         'logfile': {
#             'class': 'logging.handlers.WatchedFileHandler',
#             'filename': str(ROOT_DIR.path('runtime/logs/django.log')),
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         # Again, default Django configuration to email unhandled exceptions
#         'django.request': {
#             'handlers': ['logfile'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         # Might as well log any errors anywhere else in Django
#         'django': {
#             'handlers': ['logfile', 'console'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         # Your own app - this assumes all your logger names start with "myapp."
#         'rocket': {
#             'handlers': ['logfile'],
#             'level': 'DEBUG', # Or maybe INFO or WARNING
#             'propagate': False
#         },
#     },
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': str(ROOT_DIR.path('runtime/logs/django.log')),
        },    
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'filters': ['require_debug_true']
        }
    }
}
