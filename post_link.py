import os
import webapp2
import jinja2

from handler import *
from model.model_post import * 
from utils import *
import logging 
from cache import *

class PostLink(Handler):
    def render_post_link(self, title, content, created, user, post_id):
        hash_username = self.request.cookies.get('name')
        if read_secure_cookie(hash_username):
            username = check_secure_val(hash_username)
            logged_in = True    
        else:
            username = ""
            logged_in = False

        self.render("post.html", title=title, content=content, created=created, logged_in=logged_in, username=username, user=user, post_id=post_id)
    def get(self, post_id):
        logging.error(post_id)
        post = get_post(post_id)
            
        if post:
            title = post.title
            content = post.content
            created = post.created.strftime('%c')
            
            user = post.username
            post_id = post.key().id()
            self.render_post_link(title=title, content=content, created=created, user=user, post_id=post_id)
            
        else:
            self.render("not_found.html")