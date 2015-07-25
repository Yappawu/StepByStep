from stepbystep import db, login_manager
from datetime import datetime
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from stepbystep.models.role import RoleModel
from flask import current_app
from mongoengine import DENY, NULLIFY

from hashlib import md5

@login_manager.user_loader
def load_user(id):
    return UserModel.objects(id=id).first()


class AccountItem(db.Document):
    origin_oj = db.StringField()
    username = db.StringField(max_length=255)
    nickname = db.StringField(max_length=255)
    accept = db.StringField()
    submit = db.StringField()
    rank = db.StringField()
    solved = db.DictField()

    meta = {
        'collection': 'AccountItem'
    }

class UserModel(db.Document, UserMixin):
    username = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    roles = db.ListField(
        db.ReferenceField(RoleModel, reverse_delete_rule=DENY),
        default=[]
    )

    poj = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)
    sdut = db.ReferenceField(AccountItem, reverse_delete_rule=NULLIFY)

    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=255)
    current_login_ip = db.StringField(max_length=255)

    @staticmethod
    def generate_password(password):
        return generate_password_hash(
            current_app.config['SECRET_KEY'] + password
        )

    def set_password(self, password):
        self.password = self.generate_password(password)

    def verify_password(self, password):
        return check_password_hash(
            self.password,
            current_app.config['SECRET_KEY'] + password
        )

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        password = cls.generate_password(password)
        return cls.objects.create(
            username = username,
            password = password,
            **kwargs
        )

    def can(self, permissions):
        return True
        # TODO
        # return (self.role is not None and
                # (self.role.permissions & permissions) == permissions)

    def is_administrator(self):
        return True
        # TODO add permission
        # return self.can(Permission.ADMINISTER)

    def __unicode__(self):
        return self.username

    meta = {
        'collection': 'User'
    }

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser
