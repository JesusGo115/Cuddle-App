import webapp2
from random import shuffle
import jinja2
import os
import logging 

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
   
class InputPage(webapp2.RequestHandler):
    def get(self):
        input_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(input_template.render())

    def post(self):
        isError = False
        if isError:
            self.response.write("Error! : ( ")
        else:
            self.redirect("/")

class EchoPage(webapp2.RequestHandler):
    def get(self):
        input_template = the_jinja_env.get_template('templates/echo.html')
        self.response.write(input_template.render())
        
    def post(self):
        results_template = the_jinja_env.get_template('templates/echo.html')
        user_input = self.request.get('user-input')
        
        the_variable_dict = {"user_input_key": user_input}
        self.response.write(results_template.render(the_variable_dict)) 
        
app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/input', InputPage),
    ('/echo', EchoPage)
], debug=True)


