from flask import Blueprint
from .poj import StepPojView
from .sdut import StepSdutView


bp_step = Blueprint('step', __name__)

bp_step.add_url_rule(
    '/poj/<ordinal>',
    endpoint='poj',
    view_func=StepPojView.as_view('poj'),
    methods=['get', 'post']
)

bp_step.add_url_rule(
    '/sdut/<ordinal>',
    endpoint='sdut',
    view_func=StepSdutView.as_view('sdut'),
    methods=['get', 'post']
)
