# -*- coding: utf-8 -*-
from split_settings.tools import include

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    'components/logs.py',
    'components/suit.py',

    'components/static.py',
    'components/celery.py',
    'components/search.py',

    'components/const.py',
    'components/cache.py',
    'components/email.py',
    'components/thumb.py',
    'components/store.py',
)
