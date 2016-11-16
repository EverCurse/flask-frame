#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restful import Resource
from app.extensions import api


class apiTest(Resource):
    def get(self,user_id):
        print 'apis a'
        return {'key': 'value'}

api.add_resource(apiTest, '/api')
