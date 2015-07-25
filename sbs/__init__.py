# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

from config import config


db = MongoEngine()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

app = Flask(__name__)


with app.app_context():
    config_name = os.getenv('SBS_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .admin import flask_admin
    flask_admin.init_app(app)

    from .views import (
        bp_index,
    )

    app.register_blueprint(
        bp_index,
        url_prefix='/')
