from desabono.settings.common import *
import os

print('settings: Prod')

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "desabono"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://{name}.s3.amazonaws.com/static/'.format(name=AWS_STORAGE_BUCKET_NAME)
STATIC_URL = S3_URL
print(STATIC_URL)


# if 'RDS_HOSTNAME' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME'],
#             'PORT': os.environ['RDS_PORT'],
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'desabono',
        'USER': 'masterdb',
        'PASSWORD': 'd01m08r09',
        'HOST': 'db2.cym79uuabrv4.sa-east-1.rds.amazonaws.com',
        'PORT': '5423',
    }
}
