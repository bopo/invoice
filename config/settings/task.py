from split_settings.tools import include

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',

    'components/static.py',
    'components/celery.py',

    'components/cache.py',
    'components/thumb.py',
    'components/store.py',
)
