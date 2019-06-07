#!/usr/bin/env python

""" 
feathersToFolicles.py: Place an instance of the feather geometry under each hair folicle.
"""
import maya.cmds as cmds

def getSelected() :
    sel = cmds.ls( selection=True ) or []
    if len( sel ) < 2 :
        raise Exception('Not enough things selected. Select original feather and at least one folicle.')
    
    featherName = sel[0]
    folicleNames = sel[1:]
    
    return (featherName, folicleNames)

def feathersToFolicles() :
    featherName, folicleNames = getSelected();
    print ("Got feather name " + featherName)
    print ("Got first folicle " + folicleNames[0])
    
    for folicle in folicleNames: 
        feathInstanceName = folicle + '_feather'
        feathInstance = cmds.instance(featherName, n=feathInstanceName)
        print ( "parenting " + str(feathInstance) + " under " + str(folicle))
        cmds.parent(feathInstance, folicle)
        cmds.makeIdentity(feathInstance)#TODO get rid of warning
        cmds.rotate('180deg', 0, 0, feathInstance)

#DEBUG
print ( "Testing...")
feathersToFolicles()
