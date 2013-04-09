#!/usr/bin/env python
# coding: utf-8
__author__ = 'Snake'
import webapp2
from db import users
from weibo import APIClient
import config as c
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = urllib2.urlopen(c.weather_url, timeout=20).read()
        weather = json.loads(content)
        desc = u"大家好，今天是%s %s，温度：%s，天气：%s ，%s 明天温度:%s 天气:%s 。 - 我是每天为你勤劳预报天气的#snake的天气小助手# http://wellsnake.com" % (
            weather['weatherinfo']["date_y"],
            weather['weatherinfo']["week"],
            weather['weatherinfo']["temp1"],
            weather['weatherinfo']["weather1"],
            weather['weatherinfo']["index_d"],
            weather['weatherinfo']["temp2"],
            weather['weatherinfo']["weather2"])
        q = users.all()
        results = q.fetch(q.count())
        for r in results:
            client = APIClient(app_key=c.APP_KEY, app_secret=c.APP_SECRET,
                               redirect_uri=c.CALLBACK_URL)
            client.set_access_token(r.access_token, r.expires_in)
            client.statuses.update.post(status=desc)


app = webapp2.WSGIApplication([
                                  ('/task', MainHandler)
                              ], debug=True)
