#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager, Shell
from app import create_app
from app.models.models import Users
from app.extensions import db
app = create_app()
manage = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Users=Users)
if __name__ == '__main__':
    manage.run()
