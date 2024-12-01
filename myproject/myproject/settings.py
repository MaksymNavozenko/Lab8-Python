import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/myproject/myproject/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'myproject/staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject/static'),
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'company_db',
        'USER': 'example_user',
        'PASSWORD': 'example_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['*'] 

ROOT_URLCONF = 'myapp.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  
]

SECRET_KEY = 'lmaolmaolmao'

# settings.py
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
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Повинен бути перед AuthenticationMiddleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Повинен бути після SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Повинен бути після AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]




