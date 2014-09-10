from model.model_post import *
from google.appengine.api import memcache
import time

def get_posts(update=False):
    key = 'front'
    posts = memcache.get(key)
        
    if update or posts is None :
        posts = Post.all().order("-created")
        memcache.set(key, posts)

    return posts

def get_post(post_id, update=False):
	key = post_id
	post = memcache.get(key)

	if update or post is None:
		post=Post.get_by_id(int(key))
		memcache.set(key, post)

	return post
        