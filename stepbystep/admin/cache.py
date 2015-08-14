# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import views, flash
from flask import redirect, url_for, request  # noqa
from .mixin import BaseViewMixin
from . import admin
from flask.ext.admin import expose, expose_plugview  # noqa

from stepbystep import cache


class CacheViewAdmin(BaseViewMixin):

    @expose('/')
    def index(self):
        return self.render('admin/cache.html')

    @expose_plugview('/clear/')
    class CacheClear(views.MethodView):

        def get(self, cls):
            try:
                cache.clear()
            except:
                flash('缓存清除失败！')
            else:
                flash('缓存清除成功！')
            return redirect(url_for('admin.index'))


admin.add_view(CacheViewAdmin(name='缓存管理', url='cache'))
