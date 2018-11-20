# -*- coding: utf-8 -*-
import maya.cmds as mc

def setNode(*args):
    sec = mc.ls(sl=True, type='transform')
    print sec
    mc.textField('t1',e=True,text=sec[0])
    poseNode = mc.textField('t1',q=True,text=True)

    allnList = mc.listAttr(poseNode)
    keywd = "_init_"
    nList = []

    for x in allnList:
        if keywd in x:
            nList.append(x)

    return nList
