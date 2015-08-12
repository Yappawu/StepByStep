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

    MONGODB_SETTINGS = {
        'db': 'stepbystep',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }

    # cache
    CACHE_TYPE = 'memcached'
    CACHE_MEMCACHED_SERVERS = ['%s:%s' % (
        os.environ.get('MEMCACHED_HOST', 'localhost'),
        os.environ.get('MEMCACHED_PORT', '11211'),
    )]

    # redis
    REDIS_URL = 'redis://%s:%s/%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379'),
        os.environ.get('REDIS_DATABASE', '1'),
    )

    # celery
    CELERY_BROKER_URL = 'redis://%s:%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379'))

    CELERYBEAT_SCHEDULE = {
        'sdut_schedule': {
            'task': 'stepbystep.libs.tasks.sdut_schedule',
            'schedule': crontab(hour="*/12"),
        },
        'poj_schedule': {
            'task': 'stepbystep.libs.tasks.poj_schedule',
            'schedule': crontab(hour="*/6"),
        },
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
