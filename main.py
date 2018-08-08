import webapp2
from random import shuffle
import jinja2
import os
#from models import Meme

#from util.sessions import Session



#libraries for APIs
from google.appengine.api import urlfetch
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class StartPage(webapp2.RequestHandler):
    def get(self):
      about_template = the_jinja_env.get_template('templates/start.html')
      self.response.write(about_template.render())

class SignInPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/signin.html')
        self.response.write(about_template.render())
        
class SignUpPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/signup.html')
        self.response.write(about_template.render())
        
'''class MainInterface(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/main_interface.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("Received a post request")
'''

class InterfacePage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/interface.html')
        self.response.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/signup', SignUpPage),
    ('/interface', InterfacePage),
], debug=True)


