import webapp2
import hashlib
import jinja2
import os
from google.appengine.ext import db
from utils import *
from handler import *
from utils import *
from model.model_user import *

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")


class LoginHandler(Handler):
    def render_post_form(self, username="", login_error=""):
        self.render("login.html", username=username, login_error=login_error)

    def get(self):
        self.render_post_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        username_error = ""
        password_error = ""
        
        if valid_username(username) and valid_password(password):
            try:
                username_db =  User.get_by_user(username)[0].username
                password_db = User.get_by_user(username)[0].password
                if valid_pw(username, password, password_db):
                    cookie_val = str(make_secure_val(username))
                    self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/'%('name', cookie_val))
                    self.redirect("/")
            except Exception, e:
                login_error = "Invalid login"
                self.render_post_form(username=username, login_error=login_error)         

        else:
            login_error = "Invalid login"
            self.render_post_form(username=username, login_error=login_error)

class LogoutHandler(Handler):
    def get(self):
        self.response.headers.add_header('Set-Cookie', 'name=; Path=/')    
        self.redirect('/')    

        
            

