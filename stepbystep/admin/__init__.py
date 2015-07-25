from flask.ext.admin import Admin, AdminIndexView as _AdminIndexView
from flask.ext.login import current_user

class AdminIndexView(_AdminIndexView):
    def is_accessible(self):
        return (current_user.is_authenticated()
            and current_user.is_administrator())

admin = Admin(name = 'StepByStep',
    index_view=AdminIndexView(name='Index'),
    base_template='admin/base.html',
    template_mode='admin'
)
