from flask import Blueprint
from .statistics import StatisticsAllView


bp_statistics = Blueprint('statistics', __name__)

bp_statistics.add_url_rule(
    '/',
    endpoint='all',
    view_func=StatisticsAllView.as_view('all'),
    methods=['get']
)
