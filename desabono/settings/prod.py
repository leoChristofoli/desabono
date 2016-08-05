from desabono.settings.common import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "desabono"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'desabono',
        'USER': 'u_desabono',
        'PASSWORD': 'mydbpass',
        'HOST': 'xxxx.xxxx.ap-southeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
