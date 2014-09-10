import os
import webapp2
import jinja2

from main import *
from model.model_post import *
from utils import *

class EditPost(Handler):
    def render_new_post(self, content=""):
        self.render("new_post.html", content=content)

    def get(self, post_id):
        if logged_in():
            cookie_value = self.request.cookies.get('name')
            #from utils.py
            username = Security.check_secure_val(cookie_value) 
            if User.get_by_user(username):           
                post = Post.get_by_id(int(post_id))
                if post.username == username:
                    self.render_new_post(post.content)
        else:
            self.redirect('/login')


    def post(self, post_id):
        content = self.request.get('content')
        if not content:
            self.render_new_post(error="No Content")
        if logged_in():
            cookie_value = self.request.cookies.get('name')
            #from utils.py
            username = Security.check_secure_val(cookie_value) 
            if User.get_by_user(username):
                    post = Post.get_by_id(int(post_id))
                    if post.username == username:
                        post.content = content
                        self.redirect("/post/%d" % post_key)
                    else:
                        self.response.out.write("You can edit only your own post")

            else:
                self.redirect('/signup')

        else:
            self.redirect('/login')