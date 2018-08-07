import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())
   


class LoginPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/login.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("Received a post request")



app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/login', LoginPage),
], debug=True)


