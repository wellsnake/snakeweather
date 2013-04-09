#!/usr/bin/env python
# coding: utf-8
__author__ = 'Snake'

import webapp2
from weibo import APIClient
from db import users
import config as c


class MainHandler(webapp2.RequestHandler):
    def get(self):
        client = APIClient(app_key=c.APP_KEY, app_secret=c.APP_SECRET,
                           redirect_uri=c.CALLBACK_URL)
        url = client.get_authorize_url()    # redirect the user to `url'
        self.response.write("<a href='%s'>登录</a>" % url)

class MainHandler1(webapp2.RequestHandler):
    def get(self):
        client = APIClient(app_key=c.APP_KEY, app_secret=c.APP_SECRET,
                           redirect_uri=c.CALLBACK_URL)
        code = self.request.get('code')
        r = client.request_access_token(code)
        access_token = r.access_token  # access token，e.g., abc123xyz456
        expires_in = r.expires_in      # token expires in
        user_id = r.uid
        client.set_access_token(access_token, expires_in)
        user = users.get_by_key_name(user_id)
        if user:
            user.delete()
        e = users(access_token=access_token, expires_in=str(expires_in), key_name=user_id)
        e.put()
        self.response.write("登录成功")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

app1 = webapp2.WSGIApplication([
                                  ('/callback', MainHandler1)
                              ], debug=True)
