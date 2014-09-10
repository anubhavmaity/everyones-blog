#methods learned from the udacity course "web development" taken by steve huffman
import hashlib
import string
import random
import re
from handler import *

SECRET = '4253784905tpoihsgdsbfvndkjeugt7w653647385t4960yoihugjhfvgbioht8753rEDBACHZ'

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)
        
def valid_password(password):
    return PASSWORD_RE.match(password)
    
def valid_email(email):
    return EMAIL_RE.match(email)

def match_password(password, confirm_password):
    if password == confirm_password :
        return True
    else: 
        return False

def hash_str(s):
    h = hashlib.sha256(s).hexdigest()
    return h

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))


def make_secure_val(s):
    return "%s|%s|%s|%s" % (hash_str(s), hash_str(SECRET),s, hash_str(s))


def check_secure_val(h):
    s = h.split('|')[2]
    return s if h == make_secure_val(s) else None


# def set_secure_cookie(cls, name, val):
#     cookie_val = Security.make_secure_val(val)
#     cls.response.headers.add_header('Set-Cookie', '%s=%s; Path=/'%(name, cookie_val))

def read_secure_cookie(cookie_val):
    return cookie_val and check_secure_val(cookie_val)


def make_pw_hash( name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)
    