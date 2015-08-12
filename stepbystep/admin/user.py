# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from wtforms import fields

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import UserModel, RoleModel, AccountItem, Account
from stepbystep.libs.tasks import account_crawler


class UserAdmin(ModelViewMixin):

    column_list = [
        'name', 'roles', 'poj.user_id', 'sdut.user_id', 'created_at']
    column_filters = ['username', 'name']
    column_searchable_list = ['username', 'name']

    form_excluded_columns = [
        'password', 'created_at', 'last_login_at', 'last_login_ip',
        'current_login_at', 'current_login_ip']

    form_subdocuments = {
        'poj': {
            'form_columns': ('user_id', )
        },
        'sdut': {
            'form_columns': ('user_id', )
        }
    }

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = fields.StringField('Password')
        return form_class

    def on_model_change(self, form, model):
        if len(model.password2):
            model.password = UserModel.generate_password(form.password2.data)
        elif not model.password:
            model.password = UserModel.generate_password('12345678')

        if model.sdut.user_id:
            account = AccountItem.objects(
                origin_oj='sdut',
                username=model.sdut.user_id
            ).first()
            if not account:
                account = AccountItem.objects.create(
                    origin_oj='sdut',
                    username=model.sdut.user_id
                )
            account_crawler.delay(
                origin_oj='sdut',
                username=model.sdut.user_id
            )
            model.sdut.account = account
        else:
            model.sdut = Account(user_id='')

        if model.poj.user_id:
            account = AccountItem.objects(
                origin_oj='poj',
                username=model.poj.user_id
            ).first()
            if not account:
                account = AccountItem.objects.create(
                    origin_oj='poj',
                    username=model.poj.user_id
                )
            account_crawler.delay(
                origin_oj='poj',
                username=model.poj.user_id
            )
            model.poj.account = account
        else:
            model.poj = Account(user_id='')


class RoleAdmin(ModelViewMixin):

    column_list = [
        'name', 'description', 'created_at']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['created_at']


admin.add_view(UserAdmin(
    UserModel, name='用户列表', category='用户管理', url='user'))
admin.add_view(RoleAdmin(
    RoleModel, name='角色列表', category='用户管理', url='role'))
