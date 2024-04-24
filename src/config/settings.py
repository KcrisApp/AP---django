"""
Django settings for andamento_produzione_api project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


#reading .env file
# Load environment variables from .env file
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(" ")

#User ADMIN
USERNAME = os.getenv('USERNAME')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
NAME = os.getenv('NAME')


# Build pahs inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT =  True
# SECURE_HSTS_SECONDS = 31536000  
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'clearcache',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'widget_tweaks',
   
    #Authentication
    'rest_framework.authtoken',
    'django_registration',
    'djoser',

    # Custom app
    'produzione',
    'users',
    'core',
    'administration',
    'colorfield' 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': os.getenv('SQL_ENGINE'),
    #     'NAME': os.getenv('SQL_DATABASE'), 
    #     'USER': os.getenv('SQL_USER'),
    #     'PASSWORD': os.getenv('SQL_PASSWORD'),
    #     'HOST': os.getenv('SQL_HOST'), 
    #     'PORT': os.getenv('SQL_PORT'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATE_INPUT_FORMATS = ['%d-%m-%Y']
DATE_FORMAT = ['%d-%m-%Y']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    
]



# Actual directory user files go to
MEDIA_URL = "media/"
MEDIA_ROOT = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL  =  "users.CustomUser" #Custom user
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
#DRF permission settings
REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%d/%m/%Y %H:%M",
    'DATE_FORMAT': "%Y-%m-%d",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}



DJOSER = {
    'USER_ID_FIELD': 'username',
    "SERIALIZERS": {

           'current_user': 'users.serializers.CustomUserSerializer',
           'user': 'users.serializers.CustomUserSerializer',
    },
    "HIDE_USERS":False

}

# Disable browsable api 
if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
            "rest_framework.renderers.JSONRenderer",
        )
    

# Vite - Django connection
VITE_BUILD_DIRNAME = "build"
VITE_STATIC_BUNDLE = BASE_DIR / f"static/{VITE_BUILD_DIRNAME}"
VITE_LIVE_SERVER = True



