# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.

__author__ = 'Eya-AFFES'

from adapt.intent import IntentBuilder
#Import the IntentBuilder class from Adapt. 
#Adapt is an Intent-handling engine. Its job is to understand what a user Speaks to Mycroft, 
#and to pass that information to a Skill for handling.
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
#Importing the required libraries. These 3 libraries will be required on every Skill

import serial
ser00 = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

LOGGER = getLogger(__name__)
#This section starts logging of the Skill in the mycroft-skills.log file. 
#If you remove this line, your Skill will not log any errors, and you will have difficulty debugging.

class MoveStopSkill(MycroftSkill):
    def __init__(self):
        #This method is the constructor, and the key function it has is to define the name of the Skill.
        super(MoveStopSkill, self).__init__(name="MoveStopSkill")
        
    def initialize(self):
        #initialize()function defines each of the Intents of the Skill. 
        
        #Intents defined in vocab files
        S_T_intent = IntentBuilder("STIntent").require("STKeyword").build()
        self.register_intent(S_T_intent, self.handle_S_T_intent)

        MV_B_intent = IntentBuilder("MVBIntent").require("MVBKeyword").build()
        self.register_intent(MV_B_intent,self.handle_MV_B_intent)

        MV_F_intent = IntentBuilder("MVFIntent").require("MVFKeyword").build()
        self.register_intent(MV_F_intent ,self.handle_MV_F_intent)
 """       
        MV_R_intent = IntentBuilder("MVRIntent").require("MVRKeyword").build()
        self.register_intent(MV_R_intent, self.handle_MV_R_intent)

        MV_L_intent = IntentBuilder("MVLIntent").require("MVLKeyword").build()
        self.register_intent(MV_L_intent,self.handle_MV_L_intent)
   
        MH_F_intent = IntentBuilder("MHFIntent").require("MHFKeyword").build()
        self.register_intent(MH_F_intent, self.handle_MH_F_intent)

        MH_R_intent = IntentBuilder("MHRIntent").require("MHRKeyword").build()
        self.register_intent(MH_R_intent,self.handle_MH_R_intent)

        MH_L_intent = IntentBuilder("MHLIntent").require("MHLKeyword").build()
        self.register_intent(MH_L_intent ,self.handle_MH_L_intent)
   
        M_M_intent = IntentBuilder("MMIntent").require("MMKeyword").build()
        self.register_intent(M_M_intent, self.handle_M_M_intent)

        SR_0_intent = IntentBuilder("SR0Intent").require("SR0Keyword").build()
        self.register_intent(SR_0_intent,self.handle_SR_0_intent)

        SR_1_intent = IntentBuilder("SR1Intent").require("SR1Keyword").build()
        self.register_intent(SR_1_intent,self.handle_SR_1_intent)
"""        
    def handle_MV_F_intent(self, message):
        self.speak_dialog("MV.F")
        msg="MVF"
        ser00.write(bytes(msg, 'utf-8'))
        
    def handle_MV_B_intent(self, message):
        self.speak_dialog("MV.B")
        msg="MVB"
        ser00.write(bytes(msg, 'utf-8'))
        
    def handle_S_T_intent(self, message):
        self.speak_dialog("ST")
        msg="ST"
        ser00.write(bytes(msg, 'utf-8')) 
"""        
    def handle_MV_L_intent(self, message):
        self.speak_dialog("MV.L")
        msg="MVL"
        ser00.write(bytes(msg, 'utf-8')) 
        
    def handle_MV_R_intent(self, message):
        self.speak_dialog("MV.R")
        msg="MVR"
        ser00.write(bytes(msg, 'utf-8'))

    def handle_MH_F_intent(self, message):
        self.speak_dialog("MH.F")
        msg="MHF"
        ser00.write(bytes(msg, 'utf-8'))
      
    def handle_MH_R_intent(self, message):
        self.speak_dialog("MH.R")
        msg="MHR"
        ser00.write(bytes(msg, 'utf-8')
                    
    def handle_MH_L_intent(self, message):
        self.speak_dialog("MH.L")
        msg="MHL"
        ser00.write(bytes(msg, 'utf-8'))

    def handle_M_M_intent(self, message):
        self.speak_dialog("MM")
        msg="MM"
        ser00.write(bytes(msg, 'utf-8'))
  
    def handle_SR_0_intent(self, message):
        self.speak_dialog("SR.0")
        msg="SR0"
        ser00.write(bytes(msg, 'utf-8'))
                   
    def handle_SR_1_intent(self, message):
        self.speak_dialog("SR.1")
        msg="SR1"
        ser00.write(bytes(msg, 'utf-8')) 
"""
    

    def stop(self):
        #This method tells Mycroft what to do if a stop intent is detected.
        #the pass statement is used as a placeholder; it doesn’t actually have any function. 
        #However, if the Skill had any active functionality, the stop() method would terminate 
        #the functionality, leaving the *Skill** in a known good state.
        pass


def create_skill():
    return MoveStopSkill()
