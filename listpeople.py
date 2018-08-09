from google.appengine.ext import ndb

class Peoples(ndb.Model):
    name = ndb.StringProperty(required=True)
    age = ndb.StringProperty(required=True)
    gender = ndb.StringProperty(required=True)
    number = ndb.StringProperty(required=True)
    zip_code = ndb.StringProperty(required=True)