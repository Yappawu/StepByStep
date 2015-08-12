# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from celery.schedules import crontab

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    import sys
    reload(sys)  # noqa
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = (
        os.environ.get('SECRET_KEY') or
        '\x11\xbe\xbb\xf0\x7fz\x9d\x01\x07\xa0'
        '\xd0J\xec\xbbw\nfc\xc5Q\xd0\x8cd\xf1')
    CSRF_ENABLED = True

    # mongodb
    MONGODB_DB = os.environ.get('STEPBYSTEP_DB', 'stepbystep')
    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', '')
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')
    MONGODB_HOST = os.environ.get('MONGODB_HOST', 'localhost')
    MONGODB_PORT = os.environ.get('MONGODB_PORT', '27017')

    # redis cache
    CACHE_TYPE = 'redis'
    CACHE_DEFAULT_TIMEOUT = 7200
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    CACHE_REDIS_DB = os.environ.get('REDIS_DATABASE', '1')
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')

    # celery
    CELERY_BROKER_URL = 'redis://%s:%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379')
    )

    CELERYBEAT_SCHEDULE = {
        'sdut_schedule': {
            'task': 'stepbystep.libs.tasks.sdut_schedule',
            'schedule': crontab(hour=12),
        },
        'poj_schedule': {
            'task': 'stepbystep.libs.tasks.poj_schedule',
            'schedule': crontab(hour=3),
        },
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    # mongo
    MONGODB_DB = os.environ.get('STEPBYSTEP_DB', 'dev-stepbystep')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    # mongo
    MONGODB_DB = os.environ.get('STEPBYSTEP_DB', 'test-stepbystep')


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
