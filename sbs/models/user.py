# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask.ext.login import UserMixin, AnonymousUserMixin

from sbs import db, login_manager


__all__ = [
    'UserModel',
]


class UserModel(UserMixin, db.Document):
    __tablename__ = 'user'

    username = db.StringField(max_length=255)

    def can(self, permissions):
        return True

    def is_administrator(self):
        return True

    meta = {
        'collection': 'User'
    }


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser
