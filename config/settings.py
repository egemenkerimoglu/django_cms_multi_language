from pathlib import Path

# .env Eklentisi
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Multi Language Add
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APP = [
    "modeltranslation", #django-modeltranslation -- en başta çalışması gerekiyor
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    # Resimim dosyalarının silinmesi
    'django_cleanup.apps.CleanupConfig',
    'tinymce',
    'rosetta',
    'easy_thumbnails',
]

MY_APPS = [
    'blog',
    'page',
    'product',
    'service',
]

INSTALLED_APPS = BASE_APP + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware', # Add Multi Language
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Proje Geneline templates klasörünü tanıtmak
            BASE_DIR / 'templates',
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Global değişken tanımından sonra projeye tanıtma
                'config.project_context_processors.global_pages_context',
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True




# Multi Language
LANGUAGES = (
    ('en', _('English')),
    ('tr', _('Turkish')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# Model Translation Paketi
# Model Translation’ın default yani varsayılan dilini ayarlayalım
MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'
#modelimiz hangi dillere destek verecek bunu ayarlayalım.
MODELTRANSLATION_LANGUAGES = ('tr', 'en')

MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('tr',)}

MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'tr'

MODELTRANSLATION_AUTO_POPULATE = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Statik dosyaların nerde olduğunu tanıttık
STATICFILES_DIRS = [
    BASE_DIR / "static_files",
]

# Media dosyalarını tanım  *** urls içinde de tanımlama yapılmalı
MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media_files'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Ek Paket  ** Thumbnail aliases 
THUMBNAIL_ALIASES = {
    '': {
        'thumbnail' : {'size': (400,270), 'crop': True},
        'page' : {'size': (612,408), 'crop': True},      
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '16d5fe8f6ff0f4'
EMAIL_HOST_PASSWORD = '103498c4cca425'
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL='egemen@elkomyazilim.com'