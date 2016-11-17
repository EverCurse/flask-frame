#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify
from flask import Response
from flask import json

main = Blueprint('main', __name__)
from app.models.models import Users
from flask_login import login_required
from flask_cas import login_required as c_login_required

@main.route('/')
@login_required
def index():
    return render_template('main.html')


@main.route('/get_data')
@login_required
def datatable():
    users=Users.query.all()
    res=[]
    for i in users:
        res.append({
            'username':i.username,
            'passwd_hash':i.passwd_hash,
            'last_login':i.last_login
        })
    res={'data':res}
    return jsonify(res)

@main.route('/bt')
def bt():
    res = Users.query.all()
    users = [i.username for i in res]
    return "".join(users)
