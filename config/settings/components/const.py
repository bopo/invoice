# -*- coding: utf-8 -*-

# 融云 API 参数
RONGCLOUD_APPKEY = env('RONGCLOUD_APPKEY', default='')
RONGCLOUD_SECRET = env('RONGCLOUD_SECRET', default='')

# 极光 API 参数
JPUSH_APPKEY = env('DJANGO_JPUSH_APPKEY', default='')
JPUSH_SECRET = env('DJANGO_JPUSH_SECRET', default='')
JPUSH_OPTION = {
    "apns_production": env('DJANGO_JPUSH_PRODUCTION', default=False),
    "time_to_live": 86400,
    "sendno": 12345,
}

# 微信公众号 API 参数
WECHAT_APPKEY = env('DJANGO_WECHAT_APPKEY', default='')
WECHAT_SECRET = env('DJANGO_WECHAT_SECRET', default='')
WECHAT_TOKEN = env('DJANGO_WECHAT_TOKEN', default='')
WECHAT_OPTION = {}

# 微信小程序 API 参数
WEAPPS_APPKEY = env('DJANGO_WEAPPS_APPKEY', default='')
WEAPPS_SECRET = env('DJANGO_WEAPPS_SECRET', default='')
WEAPPS_OPTION = {}

SOCIAL_AUTH_WEIBO_KEY = env('SOCIAL_AUTH_WEIBO_KEY', default='53*****29')
SOCIAL_AUTH_WEIBO_SECRET = env('SOCIAL_AUTH_WEIBO_SECRET', default='272152************81a8b3')

SOCIAL_AUTH_QQ_KEY = env('SOCIAL_AUTH_QQ_KEY', default='10*****51')
SOCIAL_AUTH_QQ_SECRET = env('SOCIAL_AUTH_QQ_KEY', default='5807************d15bd97')

SOCIAL_AUTH_WEIXIN_KEY = env('DJANGO_WECHAT_APPKEY', default='wx4fb***********599')  # 开放平台应用的APPID
SOCIAL_AUTH_WEIXIN_SECRET = env('DJANGO_WECHAT_SECRET', default='f1c17************08c0489')  # 开放平台应用的SECRET
SOCIAL_AUTH_WEIXIN_SCOPE = ['snsapi_login']
