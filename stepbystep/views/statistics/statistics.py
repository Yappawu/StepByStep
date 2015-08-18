# -*- coding: utf-8 -*-

from flask import (  # noqa
    request,
    redirect,
    url_for,
    abort,
    current_app,
    render_template
)

from flask.views import MethodView

from stepbystep import cache  # noqa
from stepbystep.models import RoleModel, UserModel


class StatisticsAllView(MethodView):

    template = 'statistics_all.html'

    def get(self):
        per_page = current_app.config['STATISTICS_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        role = RoleModel.objects(name='statistics').first()
        paginate = UserModel.objects(roles=role).paginate(
            page=page,
            per_page=per_page
        )
        users = paginate.items
        return render_template(
            self.template,
            users=users,
            paginate=paginate
        )
