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

class HeadSirSkill(MycroftSkill):
    def __init__(self):
        #This method is the constructor, and the key function it has is to define the name of the Skill.
        super(HeadSirSkill, self).__init__(name="HeadSirSkill")
        
    def initialize(self):
        #initialize()function defines each of the Intents of the Skill. 
        
        MH_R_intent = IntentBuilder("MHRIntent").require("MHRKeyword").build()
        self.register_intent(MH_R_intent,self.handle_MH_R_intent)

        MH_L_intent = IntentBuilder("MHLIntent").require("MHLKeyword").build()
        self.register_intent(MH_L_intent ,self.handle_MH_L_intent)
      
        MH_F_intent = IntentBuilder("MHFIntent").require("MHFKeyword").build()
        self.register_intent(MH_F_intent, self.handle_MH_F_intent)

        SR_O_intent = IntentBuilder("SROIntent").require("SROKeyword").build()
        self.register_intent(SR_O_intent,self.handle_SR_O_intent)
   
        SR_Z_intent = IntentBuilder("SRZIntent").require("SRZKeyword").build()
        self.register_intent(SR_Z_intent, self.handle_SR_Z_intent)
     
    def handle_MH_R_intent(self, message):
        self.speak_dialog("MH.R")
        msg="MHR"
        ser00.write(bytes(msg, 'utf-8'))
        
    def handle_MH_L_intent(self, message):
        self.speak_dialog("MH.L")
        msg="MHL"
        ser00.write(bytes(msg, 'utf-8'))
        
    def handle_MV_F_intent(self, message):
        self.speak_dialog("MH.F")
        msg="MHF"
        ser00.write(bytes(msg, 'utf-8')) 
    
    def handle_SR_O_intent(self, message):
        self.speak_dialog("SR.O")
        msg="SR1"
        ser00.write(bytes(msg, 'utf-8')) 
        
    def handle_SR_Z_intent(self, message):
        self.speak_dialog("SR.Z")
        msg="SR0"
        ser00.write(bytes(msg, 'utf-8'))

    def stop(self):
        #This method tells Mycroft what to do if a stop intent is detected.
        #the pass statement is used as a placeholder; it doesn’t actually have any function. 
        #However, if the Skill had any active functionality, the stop() method would terminate 
        #the functionality, leaving the *Skill** in a known good state.
        pass


def create_skill():
    return HeadSirSkill()
