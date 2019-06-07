#!/usr/bin/env python

""" 
feathersToFolicles.py? Place an instance of the feather geometry under each hair folicle.
"""

import maya.cmds as cmds

def createUI( pWindowTitle, pCallback ):
    windowID = "feathToFol1"
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID)
    
    cmds.window( windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True)
    
    #TODO

#TODO
def submitCallback():
    print ("Submited")
    
  
createUI( testWindow )
    