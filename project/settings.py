import os
from dotenv import load_dotenv
load_dotenv()

ENGINE_DB = os.getenv("ENGINE_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
NAME_DB = os.getenv("NAME_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG_MODE = os.getenv("DEBUG").capitalize()

DATABASES = {
    'default': {
        'ENGINE': ENGINE_DB,
        'HOST': HOST_DB,
        'PORT': PORT_DB,
        'NAME': NAME_DB,
        'USER': USER_DB,
        'PASSWORD': PASSWORD_DB,
    }
}

INSTALLED_APPS = ['datacenter']


DEBUG = DEBUG_MODE

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
