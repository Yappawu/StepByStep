# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from flask import redirect, url_for, request
from flask.ext.login import current_user
from flask.ext.admin import Admin, AdminIndexView as _AdminIndexView


class AdminIndexView(_AdminIndexView):
    def is_accessible(self):
        return (current_user.is_authenticated()
                and current_user.is_administrator())

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))


flask_admin = Admin(
    name='后台管理', index_view=AdminIndexView(name='主页'),
    template_mode='bootstrap3')

# from . import user  # noqa
