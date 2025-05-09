"""
Django settings for partum_inventory project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

#g SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2j-tes@g+5%*wg!^o8h49br$0^$y7=)ai32vi3&sey2r0j209_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['store.desta-auto.com','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pis_com',
    'pis_ledger',
    'pis_retailer',
    'pis_product',
    'pis_sales',
    'pis_expense',
    'pis_employees',
    'pis_supplier',
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

ROOT_URLCONF = 'partum_inventory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'partum_inventory.wsgi.application'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {


#         # 'ENGINE': 'mysql.connector.django',
#         # 'NAME': 'awakzfip_desta',
#         # 'USER': 'awakzfip_desta_user',
#         # 'PASSWORD': 'jamir1.022',
#         # 'HOST': 'localhost',
#         # 'PORT': '3306',
#         # 'ENGINE': 'django.db.backends.postgresql',
#         # 'NAME': 'desta_db_1',
#         # 'USER':'desta_user',
#         # 'PASSWORD':'jamir1.022',
#         # 'HOST':'database-2.cn1e4u5sqphf.us-east-1.rds.amazonaws.com',
#         # 'PORT':'5432'
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'awakzfip_desta_store',
#         'USER': 'awakzfip_desta_store_user',
#         'PASSWORD': 'jamir1.022',
#         'HOST': 'localhost',
#         'PORT': '3306',
    
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/app_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app_static"),
    '/var/www/static/',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root/')

