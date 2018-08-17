#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer
from flask_app import db

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    pwd = Column(String(32))