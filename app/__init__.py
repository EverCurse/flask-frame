#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import absolute_import, unicode_literals
from flask import Flask, render_template, make_response
from flask import flash
from jinja2.utils import import_string
import os
from werkzeug.contrib.cache import SimpleCache
from flask_cas import CAS
from flask_restful import Api
cas_logout_tickets=SimpleCache()
blueprints = [
    ('app.views.main:main', None),
    ('app.views.auth.auth:auth', '/auth'),
]

def create_app():
    app = Flask(__name__)
    load_config(app)
    register_blueprints(app)
    set_error_handler(app)
    load_ext(app)
    return app


def load_config(app):
    env = os.environ.get('zen_env', 'dev')
    app.config.from_object(
        'config.Prod') if env == 'prod' else app.config.from_object('config.Dev')


def load_ext(app):
    from .extensions import db
    from .extensions import login_manager
    from .extensions import cas
    from .extensions import api
    api.init_app(app)
    db.init_app(app)
    api.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

def register_blueprints(app):
    for bp_info in blueprints:
        bp = import_string(bp_info[0])
        app.register_blueprint(bp, url_prefix=bp_info[1])


def set_error_handler(app):
    @app.errorhandler(404)
    def handle_404_error(error):
        flash('code:404')
        res = make_response(
            render_template(
                'error.html',
                info='no content'),
            404)
        res.headers['key'] = 'TestValue'
        return res

    @app.errorhandler(500)
    def handle_404_error(error):
        return render_template('error.html', info='500')
