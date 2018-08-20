# -*- coding: utf-8 -*-

INTERNAL_IPS = '127.0.0.1'

INSTALLED_APPS += [
    # 'silk',
    # 'django_seed',
    # 'django_baker',
    # 'debug_toolbar',
    # 'djmoney_rates',

    # 'django_bitcoin',
]

# BITCOIND_CONNECTION_STRING = "http://bitcoinuser:password@localhost:8332"

MIDDLEWARE += [
    # 'silk.middleware.SilkyMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

JQUERY_URL = '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'

# CONFIG_DEFAULTS = {
#     # Toolbar options
#     'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
#     'INSERT_BEFORE': '</body>',
#     'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
#     'RENDER_PANELS': None,
#     'RESULTS_CACHE_SIZE': 10,
#     'ROOT_TAG_EXTRA_ATTRS': '',
#     'SHOW_COLLAPSED': False,
#     'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
#     # Panel options
#     'EXTRA_SIGNALS': [],
#     'ENABLE_STACKTRACES': True,
#     'HIDE_IN_STACKTRACES': (
#         'socketserver',
#         'threading',
#         'wsgiref',
#         'debug_toolbar',
#         'django',
#     ),
#     'PROFILER_MAX_DEPTH': 10,
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'SKIP_TEMPLATE_PREFIXES': (
#         'django/forms/widgets/',
#         'admin/widgets/',
#     ),
#     'SQL_WARNING_THRESHOLD': 500,   # milliseconds
# }
