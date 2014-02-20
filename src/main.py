
# Google app engine
#import logging
import webapp2

# Internal
from application.views import MainPage
from application.views import FormatHandler

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/format', FormatHandler)
], debug=True)