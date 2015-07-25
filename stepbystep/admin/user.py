# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import UserModel, RoleModel


class UserAdmin(ModelViewMixin):

    column_list = [
        'username', 'roles', 'poj', 'sdut', 'created_at']
    column_filters = ['username']
    column_searchable_list = ['username']

    form_excluded_columns = [
        'password', 'created_at', 'last_login_at', 'last_login_ip',
        'current_login_at', 'current_login_ip']


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
