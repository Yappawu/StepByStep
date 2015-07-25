# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import ProblemModel


class ProblemAdmin(ModelViewMixin):

    column_filters = ['origin_oj', 'problem_id']
    column_searchable_list = ['problem_id', 'origin_oj']

    form_excluded_columns = ['created_at']


admin.add_view(ProblemAdmin(
    ProblemModel, name='题目列表', category='题目管理', url='problem'))
