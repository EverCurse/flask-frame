#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cas import CAS
from flask_restful import Api
cas=CAS()
db=SQLAlchemy()
login_manager=LoginManager()
api=Api()