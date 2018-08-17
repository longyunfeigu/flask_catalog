#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_app import db
from flask_app import models

account = Blueprint('account', __name__)

@account.route('/register')
def register():
    db.session.add(models.User(name='jack', pwd='123'))
    db.session.commit()
    return ''