from google.appengine.ext import ndb

class Meme(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    img_choice = ndb.StringProperty(required=False)