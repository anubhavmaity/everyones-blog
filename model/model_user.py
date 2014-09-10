from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    email = db.EmailProperty(required = True)
    name = db.StringProperty()
    password = db.StringProperty(required = True)

    @classmethod
    def get_all(cls):
        result = db.GqlQuery("SELECT * FROM User")
        return list(result)

    @classmethod
    def get_by_user(cls, username):
        result = User.all().filter("username =", username)
        return list(result)

    @classmethod
    def get_by_email(cls, email):
        result = db.GqlQuery("SELECT * FROM User WHERE email=:1 ", email)
        return list(result)

