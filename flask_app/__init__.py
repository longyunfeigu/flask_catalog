#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from flask_app.views.account import account
from flask_app.views.user import user

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.ProConfig')
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(user, url_prefix='/user')
    Session(app)

    db.init_app(app)

    return app
