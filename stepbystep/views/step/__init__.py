from flask import Blueprint
from .poj import StepPojView


bp_step = Blueprint('step', __name__)

bp_step.add_url_rule(
    '/poj',
    endpoint = 'poj',
    view_func = StepPojView.as_view('poj'),
    methods = ['get', 'post']
)
