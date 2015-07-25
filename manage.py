#!/usr/bin/env python

from sbs import app, db
from sbs.models import UserModel
from flask.ext.script import Manager, Shell, Server

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, UserModel=UserModel)

manager.add_command("shell", Shell(make_context=make_shell_context))

server = Server(host='0.0.0.0', port='5000')
manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
