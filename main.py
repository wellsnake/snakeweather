#!/usr/bin/env python
# coding: utf-8
__author__ = 'Snake'


from google.appengine.ext import webapp
import os
from weibo import APIClient
from db import users
import config as c
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):
    def get(self):
        client = APIClient(app_key=c.APP_KEY, app_secret=c.APP_SECRET,
                           redirect_uri=c.CALLBACK_URL)
        url = client.get_authorize_url()    # redirect the user to `url'
        template_values ={
            'url':url,
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class MainHandler1(webapp.RequestHandler):
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


app = webapp.WSGIApplication([
    ('/', MainHandler)
], debug=True)

app1 = webapp.WSGIApplication([
                                  ('/callback', MainHandler1)
                              ], debug=True)
