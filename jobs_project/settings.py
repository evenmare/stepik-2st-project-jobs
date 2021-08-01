"""
Django settings for jobs_project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--p*e7+*vd3q$qb&kc_eb6u8-qm+!c105-n^nqe27xjn%%0y$4&'

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'crispy_forms',
    'taggit',
    'phonenumber_field',
    'job_app',
    'authentifiaction_app',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jobs_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'job_app.context_processor.default_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'jobs_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CARDS_ON_PAGE = 10
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
MEDIA_COMPANY_IMAGE_DIR = 'company_images'
MEDIA_SPECIALITY_IMAGE_DIR = 'speciality_images'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/login'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'daeik1zwd',
    'API_KEY': '998398133394691',
    'API_SECRET': 'TgaFq-lmM93BgEimR7xBPjj8fAo',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
