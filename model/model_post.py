from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add = True)
    username = db.StringProperty(required=True)
    last_modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_all(cls):
        result = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
        return list(result)

    @classmethod
    def get_all_by_username(cls, username):
        result = Post.all().filter('username =', username)
        return list(result)

