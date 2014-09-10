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
# the handler class definition taken from udacity course "web development" taught by steve huffman
import os
import webapp2
import jinja2

from new_post import *
from edit_post import *
from handler import *
from login import *
from utils import *
from signup import *
from post_link import *
from cache import *



class MainHandler(Handler):
    def render_front_page(self, posts=""):
        hash_username = self.request.cookies.get('name')
        if read_secure_cookie(hash_username):
            username = check_secure_val(hash_username)
            logged_in = True
        else:
            username = ""
            logged_in = False

        self.render('front.html',logged_in=logged_in, username=username, posts=posts)
    
    def get(self):
        posts = list(get_posts())
        self.render_front_page(posts=posts)
        

    

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/new_post', NewPost), ('/edit_post/%d', EditPost), ('/login', LoginHandler), ('/signup', SignupHandler), ('/logout', LogoutHandler), ('/post_(\d+)', PostLink)
], debug=True)
