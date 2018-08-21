# -*- coding: utf-8 -*-

INSTALLED_APPS = ["suit", 'django.contrib.admin',] + INSTALLED_APPS + [
    'mptt',
]

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'路书发票管理系统',
    'HEADER_DATE_FORMAT': 'Y F j l',
    'HEADER_TIME_FORMAT': 'Y-m-d H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': '认证', 'icon': 'icon-lock', 'models': ('user', 'group')},
    #     {'label': '资源管理', 'icon': 'icon-cog', 'models': ('restful.restauth', 'restful.stars','restful.brand')},
    #     {'label': '设置', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': '支持', 'icon': 'icon-question-sign', 'url': '/admin/doc/'},
    # ),

    # misc
    'LIST_PER_PAGE': 15,
}

if not DEBUG:
    SUIT_CONFIG['MENU_EXCLUDE'] = ('auth.group',)
    SUIT_CONFIG['MENU'] = (
        'sites',
        {'app': '认证', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'label': '资源', 'icon': 'icon-cog', 'models': ('service.kernel',)},
        {'label': '设置', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': '支持', 'icon': 'icon-question-sign', 'url': '/admin/doc/'},
    )
