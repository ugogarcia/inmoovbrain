__author__ = 'Ugo'
import re
import os
import sys
import xml.etree.ElementTree as etree

class ChatRuntime:
    def __init__(self):
        self.context=""
        self.lastInput=""
        self.lastRegExp=""
        self.rightWildcard=""
        self.month=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        self.weekday=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
        self.commandsDatabase = []
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        xmltree=etree.parse(application_path+'/chatbot.xml')
        xmlroot=xmltree.getroot()
        for xmlchild in xmlroot:
            if xmlchild.tag=="language":
                for sentence in xmlchild.findall('sentence'):

                    command=[]
                    obj=sentence.find('id')
                    if obj is not None:
                        if obj.text is not None:
                            command.append(obj.text)
                        else:
                            command.append('')
                    else:
                        command.append('')
                    obj=sentence.find('pattern')
                    if obj is not None:
                        command.append(obj.text)
                    obj=sentence.find('context')
                    if obj is not None:
                        if obj.text is not None:
                            command.append(obj.text)
                        else:
                            command.append('')
                    else:
                        command.append('')
                    obj=sentence.find('response')
                    if obj is not None:
                        command.append(obj.text)
                    else:
                        print ("ERROR IN XML")

                    self.commandsDatabase.append(command)

    def respond (self, input):
        index=0
        input=input.lower()
        self.lastInput=input

        for command in self.commandsDatabase:
            if command[2]==self.context or command[2]=="":
                p = re.compile(command[1], re.IGNORECASE)
                if p.match(input)!=None:
                    self.context=command[0]
                    self.lastRegExp=command[1]
                    self.fillCommandAtributes()
                    return command[3]
        self.context=""
        self.lastRegExp=""
        return (None)

    def fillCommandAtributes(self):
        # (.*) derecha
        if self.lastRegExp[-4:]=="(.*)":
            right_text=re.sub(self.lastRegExp[0:-4],"", self.lastInput)
            self.rightWildcard=right_text.strip()
        else:
            self.rightWildcard=""
        return