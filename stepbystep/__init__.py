#-*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Mail
from flask.ext.security import Security, MongoEngineUserDatastore
from config import config

app = Flask(__name__)
db = MongoEngine()
mail = Mail()
login_manager = LoginManager()
security = Security()

with app.app_context():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from stepbystep.models import UserModel, RoleModel
    user_datastore = MongoEngineUserDatastore(db, UserModel, RoleModel)

    security.init_app(app, user_datastore)

    from .views import (
        bp_index,
    )

    app.register_blueprint(
        bp_index,
        url_prefix='/'
    )
