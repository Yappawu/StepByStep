# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from celery.schedules import crontab


class Config(object):

    SECRET_KEY = (
        os.environ.get('SECRET_KEY') or
        '\x11\xbe\xbb\xf0\x7fz\x9d\x01\x07\xa0'
        '\xd0J\xec\xbbw\nfc\xc5Q\xd0\x8cd\xf1')

    MONGODB_SETTINGS = {
        'db': 'StepByStep',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }
    SQLALCHEMY_RECORD_QUERIES = True
    # SQLALCHEMY_ECHO = True

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
        'test': {
            'task': 'sbs.core.tasks.test',
            'schedule': crontab(minute='*/1'),
            'args': (1, 2, 3)
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
