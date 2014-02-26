
# Python
import traceback

# BeautifulSoup
from bs4 import BeautifulSoup

# Google app engine
import logging
from webapp2 import RequestHandler

# Internal
import utils
from format import XmlFormatter

class MainPage(RequestHandler):    
    def get(self):
        utils.render_template(self, 'index.html')
      
class FormatHandler(RequestHandler):
    def post(self):        
        try:
            xml = self.request.get("xml")
            fixupXml = self.request.get("fixupXml").lower() == "true" 
            #logging.info("XML: " + xml)
            #logging.info("FixupXml: " + fixupXml.str())
            
            #soup = BeautifulSoup(xml, "html.parser")        
            #formattedXml = soup.prettify(formatter=None);
            
            if (fixupXml):
                soup = BeautifulSoup(xml, "html.parser")        
                formattedXml = soup.prettify(formatter=None);
            else:                        
                formatter = XmlFormatter()
                formattedXml = formatter.format(xml)        
                
            self.response.out.write(formattedXml)                    
        except Exception as ex:
            logging.error(traceback.format_exc())
                                                
            self.response.set_status(500, str(ex))
            self.response.out.write(str(ex))
            
        #logging.info("sent response")
                    