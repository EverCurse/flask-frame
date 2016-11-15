#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
main = Blueprint('main', __name__)
from app.models.models import Users
from flask_login import login_required


@main.route('/')
@login_required
def index():
    return render_template('main.html')


@main.route('/bt')
def bt():
    res = Users.query.all()
    users = [i.username for i in res]
    return "".join(users)
