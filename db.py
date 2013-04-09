#!/usr/bin/env python
# coding: utf-8
__author__ = 'Snake'

from google.appengine.ext import db


#用户表
class users(db.Model):
    access_token = db.StringProperty(required=True)
    expires_in = db.ByteStringProperty(required=True)
