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
   


class InfoPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/info.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("Received a post request")
        
class MainInterface(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/main_interface.html')
        self.response.write(about_template.render())
    def post(self):
        self.response.write("Received a post request")



app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/info', InfoPage),
    ('/main', MainInterface),
], debug=True)


