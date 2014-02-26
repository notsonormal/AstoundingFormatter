import os

from google.appengine.ext.webapp import template     

def render_template(request_handler, template_name, template_values = dict()):
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')   
    path = os.path.join(template_dir, template_name)
    
    request_handler.response.out.write(template.render(path, template_values))    