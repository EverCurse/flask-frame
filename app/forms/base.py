#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Required,Length
class LoginForm(Form):
    username=StringField('username',validators=[
        DataRequired(),
        Length(6,18)
    ])

    password=StringField('password',validators=[
        DataRequired(),
        Length(3,16)
    ])

