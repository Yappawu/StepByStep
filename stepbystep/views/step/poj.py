# -*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user, login_required

from stepbystep.models import ProblemModel

class StepPojView(MethodView):

    template = 'step/poj.html'

    def get(self):
        problems = ProblemModel.objects(origin_oj='poj')
        return render_template(self.template, problems=problems)

    def post(self):
        pass
