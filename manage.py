# -*- coding: utf-8 -*-

from stepbystep import app, db
from flask.ext.script import Manager, Server, Shell

from stepbystep.models import UserModel, RoleModel

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, UserModel=UserModel, RoleModel=RoleModel)

manager.add_command(
    "runserver", Server(
        use_debugger=True,
        use_reloader=True,
        host="0.0.0.0",
        port=4000
    )
)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    RoleModel.insert_roles()
    admin = RoleModel.objects(name='admin').first()

    user = UserModel.create_user(
        username='admin',
        name='admin',
        password='admin'
    )
    user.roles.append(admin)
    user.save()


if __name__ == '__main__':
    manager.run()
