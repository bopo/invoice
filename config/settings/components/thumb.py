# -*- coding: utf-8 -*-

# INSTALLED_APPS += [
#     "django_thumbor",
# ]

# INSTALLED_APPS += ('easy_thumbnails',)

# THUMBNAIL_ALIASES = {
#     '': {
#         'avatar': {'size': (50, 50), 'crop': True},
#     },
# }

# THUMB_LIST = '500x500'
# THUMB_DETAIL = '800x800'

# The host serving the thumbor resized images
THUMBOR_SERVER = 'http://localhost:8888'

# The prefix for the host serving the original images
# This must be a resolvable address to allow thumbor to reach the images
THUMBOR_MEDIA_URL = 'http://localhost:8888/media'

# If you want the static to be handled by django thumbor
# default as False, set True to handle it if you host your statics
THUMBOR_STATIC_ENABLED = False

# The prefix for the host serving the original static images
# this must be a resolvable address to allow thumbor to reach the images
THUMBOR_STATIC_URL = 'http://localhost:8888/static'

# The same security key used in the thumbor service to
# match the URL construction
THUMBOR_SECURITY_KEY = 'MY_SECURE_KEY'

# Default arguments passed to the `generate_url` helper or
# the `thumbor_url` templatetag
THUMBOR_ARGUMENTS = {}

# An alias represents a named set of arguments to the generate_url function
# or thumbor_url template tag. Use it to share general thumbnail
# configurations without repeating yourself.
THUMBOR_ALIASES = {}
