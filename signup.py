#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import hashlib
import jinja2
import os
from google.appengine.ext import db
from model.model_user import *
from utils import *
import logging
from handler import Handler



class SignupHandler(Handler):

    def render_post_form(self, username="", username_error="", username_exists="", password_error="", password_unmatch="", email="", email_error=""):
        self.render("signup.html", username=username, username_error=username_error, username_exists=username_exists, password_error=password_error, password_unmatch=password_unmatch, email=email, email_error=email_error)

    def get(self):
        self.render_post_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        confirm_password = self.request.get('verify')
        email  = self.request.get('email')

        username_error = ""
        password_error = ""
        password_unmatch = ""
        email_error = ""
        username_exists = ""

        # username_db = db.GqlQuery("SELECT * FROM Signup WHERE username=:1 LIMIT 1", username)
        # for i in username_db:
        #     if i.username == username:
        #        username_exists = "username already exists" 

        #removed the valid email portion
        if (valid_username(username) and valid_password(password) and match_password(password, confirm_password)):
            
            try:
                username_db= User.get_by_user(username)[0].username
                
            except Exception, e:
                username_db = ""
            

                
            if username_db == username:
                username_exists = "username already exists"
            else:   
                password = make_pw_hash(username, password)
                user = User(username=username, password=password, email=email)
                user.put()
                cookie_val = str(make_secure_val(username))
                self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/'%('name', cookie_val))
                self.redirect("/")

        else:
            if not valid_username(username):
                username_error = "Username Invalid"
            if not valid_password(password):
                password_error = "Password Invalid"
            if not match_password(password, confirm_password):
                password_unmatch = "Passwords doesn't match"
            # if not valid_email(email):
            #     email_error = "Email Invalid"

        self.render_post_form(username, username_error, username_exists, password_error, password_unmatch, email, email_error)    


        


