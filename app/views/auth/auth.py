#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Blueprint, render_template, request, current_app, flash, redirect, jsonify
from flask import url_for
from flask_login import login_user
from app.extensions import db
auth = Blueprint('auth', __name__)
from app.models.models import Users
from app.views.auth.passwd import check_password, gen_passwd_hash
from flask_login import login_required, logout_user


def cas_login():
    return 'cas'


def local_login():
    username = request.values.get('username', None)
    password = request.values.get('password', None)
    user = Users.query.filter_by(username=username).first()
    if user:
        if user.is_confirm == 1:
            if check_password(user, password):
                login_user(user)
                user.last_login = datetime.now()
                db.session.add(user)
                db.session.commit()
                return redirect(request.args.get('next') or url_for("main.index"))
            else:
                flash(u'  认证失败')
                return render_template('auth/login.html')
        else:
            flash(u'  账户未激活，请联系管理员激活')
            return render_template('auth/login.html')
    else:
        flash(u'  用户不存在')
        return render_template('auth/login.html')


@auth.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        if current_app.config['USE_CAS']:
            return cas_login()
        else:
            return local_login()


@auth.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        username = request.values.get('username', None)
        password = request.values.get('password', None)
        user = Users.query.filter_by(username=username).first()
        if user:
            return jsonify({'code': 300, 'data': '用户名已存在'})

        else:
            password = gen_passwd_hash(password)
            user = Users(username=username, passwd_hash=password,is_confirm=0,reg_time=datetime.now(),role=0)
            db.session.add(user)
            db.session.commit()
            return jsonify({'code': 200, 'data': '注册成功，请登录'})


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
