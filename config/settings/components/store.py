# -*- coding: utf-8 -*-

AWS_S3_SIGNATURE_VERSION = env('DJANGO_MINIO_VERSION', default='s3v4')
AWS_S3_ENDPOINT_URL = env('DJANGO_MINIO_ENCRYPTION', default='http://127.0.0.1:9000')
AWS_S3_REGION_NAME = env('DJANGO_MINIO_REGION', default='us-east-1')
AWS_S3_ENCRYPTION = env('DJANGO_MINIO_ENCRYPTION', default=False)

AWS_ACCESS_KEY_ID = env('DJANGO_MINIO_ACCESSKEY', default='O21TSRP1HLRNR84YU0QV')
AWS_SECRET_ACCESS_KEY = env('DJANGO_MINIO_SECRETKEY', default='+VPu5glwaD8fXLJKJ8kLQOZDC/nEfKKvXuJXh2we')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_MINIO_BUCKET', default='storage')

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# ================================

QINIU_ACCESS_KEY = env('DJANGO_QINIU_ACCESS_KEY', default='zPObn7m8F5RZ1dF9kth4Wivz7WE89rWL1sA_Zt')
QINIU_SECRET_KEY = env('DJANGO_QINIU_SECRET_KEY', default='sLdn1AkrebELj-vdFIZs6cmV3LRP13P-qShZEf')
QINIU_SECURE_URL = False      #使用http 

QINIU_BUCKET_NAME = env('DJANGO_QINIU_BUCKET_NAME', default='wj5633')
QINIU_BUCKET_DOMAIN = env('DJANGO_QINIU_BUCKET_DOMAIN', default='ompehspge.bkt.clouddn.com/')

# PREFIX_URL = 'http://'

# MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'

# ==================================

ACCESS_KEY_ID = "40ZhE1HyuWdllpMh"
ACCESS_KEY_SECRET = "KbxtlKSvKyuyuymTiQvrxhsYFMguXy"
END_POINT = "oss-us-west-1.aliyuncs.com"
BUCKET_NAME = "XXXX"
ALIYUN_OSS_CNAME = "" # 自定义域名，如果不需要可以不填写
BUCKET_ACL_TYPE = "private" # private, public-read, public-read-write

# mediafile将自动上传
# DEFAULT_FILE_STORAGE = 'aliyun_oss2_storage.backends.AliyunMediaStorage'
# staticfile将自动上传
# STATICFILES_STORAGE = 'aliyun_oss2_storage.backends.AliyunStaticStorage'
