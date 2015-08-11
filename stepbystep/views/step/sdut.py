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

from stepbystep.models import ProblemModel, RoleModel, UserModel, CategoryModel

ORDINAL = {
    'program_1': 0,
    'program_2': 1,
    'data_structure': 2
}


class StepSdutView(MethodView):

    template = 'step.html'

    def get(self, ordinal):
        role = RoleModel.objects(name=ordinal).first()
        ordinal = CategoryModel.objects.get_or_404(
            ordinal=ORDINAL.get(ordinal), origin_oj='sdut')
        problems = ProblemModel.objects(
            origin_oj='sdut', genera=ordinal).order_by('ordinal').all()
        users = UserModel.objects(roles__0=role).all()

        return render_template(
            self.template,
            problems=problems,
            users=users,
            ordinal=ordinal
        )
