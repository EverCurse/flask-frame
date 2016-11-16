#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restful import Resource, Api
from flask import Flask
app = Flask(__name__)
api = Api(app)


class Test(Resource):

    def get(self):
        return {'key': 'value'}
api.add_resource(Test, '/apis/users')
if __name__ == '__main__':
    app.run()
