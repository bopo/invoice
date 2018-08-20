# -*- coding: utf-8 -*-

MIDDLEWARE += (
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': ROOT_DIR.path('runtime/cache').__str__(),
    },
    # 'locmem': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake',
    # },
    # 'dummy': {
    #     'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    # },
    # 'redis': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': '127.0.0.1:6379',
    #     'OPTIONS': {
    #         'DB': 0,
    #         'PASSWORD': '',
    #         'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
    #         'CONNECTION_POOL_CLASS_KWARGS': {
    #             'max_connections': 50,
    #             'timeout': 20,
    #         }
    #     },
    # },
    # 'memcache': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '127.0.0.1:11211',
    #     'LOCATION': 'unix:/tmp/memcached.sock',
    # },
    # 'database': {
    #     'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    #     'LOCATION': 'my_cache_table',
    # }
}

REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60
