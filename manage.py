# -*- coding: utf-8 -*-
import random

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
    username = 'admin%s' % random.randint(1, 0xffffff)
    password = username
    UserModel.create_user(
        username=username,
        password=password
    )
    print 'username: %s, password: %s' % (username, password)


if __name__ == '__main__':
    manager.run()
