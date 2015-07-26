# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import CategoryModel


class CategoryAdmin(ModelViewMixin):

    column_list = ['name', 'created_at']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['created_at']

    form_ajax_refs = {
        'parent': {
            'fields': ['name'],
            'allow_blank': True,
        }
    }


admin.add_view(CategoryAdmin(
    CategoryModel, name='分类列表', category='分类管理', url='category'))
