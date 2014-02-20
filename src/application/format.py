from cStringIO import StringIO
import os
import re

class XmlFormatter(object):
    
    def __init__(self):
        self.indent = 0

    def getNextCharacter(self, xml, index):
        if (len(xml) > index + 1):
            return xml[index + 1]
        return None
    
    def getPreviousCharacter(self, xml, index):
        if (len(xml) > index - 1):
            return xml[index - 1]
        return None    

    def indentXml(self, xml):
        if (self.indent >= 0):
            xml.write("\t" * self.indent) 
        return xml
    
    def getIndent(self):
        if (self.indent >= 0):
            return "\t" * self.indent
        return ""

    def logMessage(self, message):
        #print(message)
        pass    
    
    def formatNew(self, xml):
        
        interestingPattern = re.compile('[&<]')
        startTagOpenPattern = re.compile('<[a-zA-Z]')
        
        # SEE bs4.HTMLParser goahead function
        
        i = 0        
        length = len(xml)              
        
        while i < length:
            match = interestingPattern.search(xml, i)
            if match:
                j = match.start()
            else:
                j = length
                
            if i == length:
                break
            
            if xml.startswith('<', i):
                pass
              
        
    def format(self, unformattedXml):
        
        # TODO: This seems to be cutting off the end of the string somewhere for some reason?
        # 2500 lines instead of 5000?
        
        formattedXml = StringIO()
        
        # Remove any whitespace, tabs and newlines already in the unformatted XML
        pattern = re.compile('\s+')        
        unformattedXml = pattern.sub('', unformattedXml)        
        
        for index, character in enumerate(unformattedXml):

            #self.logMessage(character)

            #beginTag = False
            #endTag = False        

            if (character == '<' and self.getNextCharacter(unformattedXml, index) == '/'):
                self.logMessage("GET END TAG")
                #endTag = True                

                self.indent -= 1                
                formattedXml.write("\n")
                
                self.indentXml(formattedXml)
                formattedXml.write(character)
            elif (character == '<' and self.getNextCharacter(unformattedXml, index) == '-' 
                  and self.getNextCharacter(unformattedXml, index + 1) == '-'):
                # Start comment, i.e <!--
                formattedXml.write(character)
            elif (character == '<'):
                self.logMessage("GET BEGIN TAG")
                #beginTag = True

                self.indent += 1                
                formattedXml.write(character)                
            elif (character == '>' and self.getPreviousCharacter(unformattedXml, index) == '-' 
                  and self.getPreviousCharacter(unformattedXml, index - 1) == '-'):
                # End comment, i.e. -->
                formattedXml.write(character)
            elif (character == '>'):
                self.logMessage("GOT END TAG")
                                
                #if (beginTag):
                #    self.logMessage("CLOSE BEGIN TAG")
                #   self.indent += 1
                #    beginTag = False
                    
                #if (endTag):
                #    self.logMessage("CLOSE END TAG")
                #    self.indent -= 1
                #    endTag = False
                            
                formattedXml.write(character)                            
                formattedXml.write("\n")                    
                self.indentXml(formattedXml)
            elif (character == "/" and self.getNextCharacter(unformattedXml, index) == '>'):
                # Handling self-closing tags, e.g. <name />
                formattedXml.write(character)
                self.indent -= 1           
            else:
                formattedXml.write(character)
                    
        # Remove empty lines, or lines with just tabs
        text = os.linesep.join([s for s in formattedXml.getvalue().splitlines() if s.strip(' \t\n\r')])
        #text = formattedXml.getvalue()
    
        formattedXml.close()
        
        return text           
         
