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
   


class ContactPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/contact.html')
        self.response.write(about_template.render())
   
    def post(self):
        isError = False
        if isError:
            self.response.write("Error! : ( ")
        else:
            self.redirect("/")
    
app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/contact', ContactPage),
], debug=True)


