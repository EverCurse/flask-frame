#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .extensions import db
from flask_login import UserMixin

class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    username = db.Column(db.String(256), nullable=False)
    passwd_hash = db.Column(db.String(256), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Users %r>' %self.username


from .extensions import login_manager
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)