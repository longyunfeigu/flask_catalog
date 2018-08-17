#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_app import db

user = Blueprint('user', __name__)

@user.route('/get_info')
def get_info():
    return ''