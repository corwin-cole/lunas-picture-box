"""
Django settings for lpb project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'lpb-env.us-west-1.elasticbeanstalk.com',
    '172.31.164.87',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'storages',
    'taggit',
    'taggit_templatetags2',
    'fontawesome',
    'django_countries',
    'phonenumber_field',
    'main_site_content.apps.MainSiteContentConfig',
    'photos.apps.PhotosConfig',
]

AWS_S3_REGION_NAME = 'us-west-1'
STATIC_AWS_STORAGE_BUCKET_NAME = os.environ.get('STATIC_AWS_STORAGE_BUCKET_NAME')
STATIC_AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(STATIC_AWS_STORAGE_BUCKET_NAME)
MEDIA_AWS_STORAGE_BUCKET_NAME = os.environ.get('MEDIA_AWS_STORAGE_BUCKET_NAME')
MEDIA_AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(MEDIA_AWS_STORAGE_BUCKET_NAME)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lpb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lpb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'PORT': os.environ.get('RDS_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Phone number field
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'

# Static files
STATIC_URL = 'https://{}/'.format(STATIC_AWS_S3_CUSTOM_DOMAIN)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'lunas_picture_box.custom_storages.StaticStorage'
MEDIA_URL = 'https://{}/'.format(MEDIA_AWS_S3_CUSTOM_DOMAIN)
DEFAULT_FILE_STORAGE = 'lunas_picture_box.custom_storages.MediaStorage'

# Email
SERVER_EMAIL = 'corwin@lunaspicturebox.com'
ADMINS = (
    ('Dana Cassity', 'dana@lunaspicturebox.com'),
    ('Corwin Cole', 'corwin@lunaspicturebox.com'),
)
CONTACT_US_RECIPIENT_EMAIL = 'corwin@lunaspicturebox.com'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
