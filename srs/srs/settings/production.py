from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'srsprod',
        'USER': 'srsadmin',
        'PASSWORD': 'srsadmin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
MEDIA_URL = 'http://45.55.131.51/media/'
MEDIA_ROOT = BASE_DIR.child('media')

STATIC_URL = 'http://45.55.131.51/staticfiles/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('static2')