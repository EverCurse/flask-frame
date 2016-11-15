#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash


def gen_passwd_hash(passwd):
    return generate_password_hash(passwd)


def check_password(user, passwd):
    return check_password_hash(user.passwd_hash, passwd)