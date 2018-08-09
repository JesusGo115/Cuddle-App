import webapp2
from random import shuffle
import jinja2
import os
from listpeople import Peoples
from google.appengine.api import urlfetch
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_all_people(self):
    all_people = Peoples.query().fetch()
        
    the_variable_dict = {
            "all_people_key": all_people
        }
    return the_variable_dict
    
def run_query(first_line, second_line, third_line, fourth_line, fifth_line):
    people = Peoples(name=first_line, age = second_line, gender = third_line, number = fourth_line, zip_code = fifth_line)
    people_key = people.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print people_key

    
    
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
        '''
        people_first_line = self.request.get('name')
        people_second_line = self.request.get('age')
        people_third_line = self.request.get('gender')
        people_fourth_line = self.request.get('number')
        people_fifth_line = self.request.get('zip')
        
        run_query(people_first_line, people_second_line, people_third_line, people_fourth_line, people_fifth_line)
        
        the_variable_dict = {"line1": people_first_line,
                             "line2": people_second_line,
                             "line3": people_third_line,
                             "line4": people_fourth_line,
                             "line5": people_fifth_line
                             }
                             '''
        self.response.write(about_template.render())

class InterfacePage(webapp2.RequestHandler):
    def post(self):
        interface_template = the_jinja_env.get_template('templates/interface.html')
        people_name = self.request.get('name')
        people_age = self.request.get('age')
        people_gender = self.request.get('gender')
        people_number = self.request.get('number')
        people_zip_code = self.request.get('zip')
        
        run_query(people_age, people_age, people_gender, people_number, people_zip_code)
        
        the_variable_dict = get_all_people(self)
    
        self.response.write(interface_template.render(the_variable_dict))
    def get(self):
        interface_template = the_jinja_env.get_template('templates/interface.html')
        
        the_variable_dict = get_all_people(self)
        
        self.response.write(interface_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/signup', SignUpPage),
    ('/interface', InterfacePage),
    ('/signin', SignInPage)
], debug=True)


