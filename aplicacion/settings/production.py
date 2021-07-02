from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['administrador-predios.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3modeo8s86cc2',
        'USER': 'ursqoezpcnunmc',
        'PASSWORD': 'af8f76554a396ab8ab82ca3645b796c5582359568697732ea3e0c0c29ebfb1be',
        'HOST':'ec2-34-206-8-52.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


