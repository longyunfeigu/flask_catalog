#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
不用这个离线脚本，借助下面命令也可以创建表
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
"""

from flask_app import create_app
from flask_app import db
app = create_app()

with app.app_context():
    db.create_all()