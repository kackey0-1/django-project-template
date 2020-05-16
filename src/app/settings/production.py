"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import pymysql
import sys
from app.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c72f8m&)w6f(63cfr-7-jpm^n50a_u+)uh1r7)!w&pzmu5=9s('

# SECURITY WARNING: don't run with debug turned on in production!
# 本番稼働時にはセキュリティ面を考慮して必ずこの DEBUG を False にしておくこと
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_app',
        'USER': 'django_app',
        'PASSWORD': 'django_app',
        'HOST': 'db',
        'PORT': '3306',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'parso': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    }
}

# メール設定
# Gmail 以外の場合 EMAIL_HOST,EMAIL_PORT の変更が必要
# EMAIL_HOST_USER に送信元のメールアドレスを入力する
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ideal.asp.contact@gmail.com'
EMAIL_HOST_PASSWORD = 'contactideal123'

EMAIL_USE_TLS = True

SHELL_PLUS = "ipython"
IPYTHON_ARGUMENTS = [
  '--profile-dir', '/code/ipython_profile'
]
