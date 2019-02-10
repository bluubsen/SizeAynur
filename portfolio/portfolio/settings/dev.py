from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "aynurotakmaz",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}
