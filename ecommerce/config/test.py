#==== DEVELOPMENT MODE =====
DEBUG = True

#if DEBUG is False:
#    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
#else:
#    ALLOWED_HOSTS = []

from .base import *

ALLOWED_HOSTS = ["127.0.0.1", "localhost"] if DEBUG is False else ["0.0.0.0", "192.168.1.4", "127.0.0.1"]
# Application definition

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE' : "django.db.backends.mysql",
        #"NAME" : "",
        #"USER": "",
        #"PASSWORD": "",
        #"HOST": "",
        #"PORT": "",
    }

}

TIME_ZONE = 'Asia/Manila'

#Email Configuration
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = "someone@example.com" # Sender Email
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "Admin <{}>".format(EMAIL_HOST_USER)

