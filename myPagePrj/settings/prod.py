from .base import *
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=".env")

DEBUG = env('DJANGO_PROD_DEBUG_MODE')

ALLOWED_HOSTS = env.list('DJANGO_PROD_ALLOW_HOST')

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DJANGO_PROD_DB_ENGINE'),
        'NAME': BASE_DIR / env('DJANGO_PROD_DB_NAME'),
    }
}