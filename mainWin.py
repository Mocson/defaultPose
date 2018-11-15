# -*- coding: utf-8 -*-

# Add Script Path #
import sys
scriptPath = r'filePath/defaultPose'
if not scriptPath in sys.path:
    sys.path.append(scriptPath)

# import #
import maya.cmds as mc
import saveDefaultPose
import setDefaultPose
import setNode

#=== Reload Files ===#
reload(saveDefaultPose)
reload(setDefaultPose)
reload(setNode)

#====================#

nList = []

def addnList(*args):
    global nList
    nList = setNode.setNode()

def set(*args):
    setDefaultPose.setDefaultPose(atList=nList)

# Window #
def winDefaultPose():
    if mc.window('ioDefaultPose', exists=True):
        mc.deleteUI('ioDefaultPose')

    win = mc.window('ioDefaultPose',title='ioDefaultPose',width=200)
    mc.columnLayout(adj=True)
    mc.textField('t1',w=95,pht='defaultPose1')
    mc.button(label="saveDefaultPose", command = saveDefaultPose.saveDefaultPose)
    mc.button(label="setDefaultPose", command = set)
    mc.button(label="setPoseNode", command = addnList)
    mc.showWindow(win)

winDefaultPose()
