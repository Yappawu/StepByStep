import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = 'you-will-never-guess'
    CSRF_ENABLED = True
    MONGODB_SETTINGS = {
        'db': 'stepbystep',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }

    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
