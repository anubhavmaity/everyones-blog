import os
import webapp2
import jinja2

from main import *
from model.model_user import *
import webapp2
import jinja2
from utils import *
from main import *
from model.model_post import *
from utils import *
from handler import *
from cache import *
import time

import logging
import sys
logging.error(sys.path)

class NewPost(Handler):
    def render_new_post(self, title="", content="",logged_in=False, username="", error=""):
        hash_username = self.request.cookies.get('name')
        if read_secure_cookie(hash_username):
            username = check_secure_val(hash_username)
            logged_in= True
        else:
            self.redirect('/login')

        self.render("new_post.html", title=title, content=content, logged_in=logged_in, username=username, error=error)

    def get(self):
        self.render_new_post()

    def post(self):
        title = self.request.get('title')
        content = self.request.get('content')
        
        if not title and not content:
            self.render_new_post(error="No Title and No Content")
            
        if not title:
            self.render_new_post(error="No Title", content=content)
        if not content:
            self.render_new_post(error="No Content", title=title)

        hash_username = self.request.cookies.get('name')
        if read_secure_cookie(hash_username):
            #from utils.py
            username = str(check_secure_val(hash_username))
            logging.error(username)
            
            if User.get_by_user(username):
                username_db = User.get_by_user(username)[0].username
                logging.error(username_db)
                if username_db:
                    content = content.replace('\n', '<br>')
                    post = Post(title=title, content = content, username=username)
                    post_key = post.put().id()
                    get_posts(update=True)
                    
                    self.redirect("/post_%d" % post_key)

            else:
                self.redirect('/signup')

        else:
            self.redirect('/login')

        

