# -*- coding: utf-8 -*-
import maya.cmds as mc

def saveDefaultPose(*args):
    sec = mc.ls(sl=True, type='transform')
    nodeName = mc.textField('t1',q=True,text=True)
    print nodeName

    cNodeName = mc.createNode('transform',n=nodeName)
    print cNodeName

    for i in sec:
        tx = mc.getAttr(i + '.translateX')
        ty = mc.getAttr(i + '.translateY')
        tz = mc.getAttr(i + '.translateZ')
        rx = mc.getAttr(i + '.rotateX')
        ry = mc.getAttr(i + '.rotateY')
        rz = mc.getAttr(i + '.rotateZ')

        mc.addAttr(cNodeName, ln='{}_init_translateX'.format(i), at='float', dv=tx)
        mc.setAttr(cNodeName + '.{}_init_translateX'.format(i), e=True, keyable=False, lock=True)
        mc.addAttr(cNodeName, ln='{}_init_translateY'.format(i), at='float', dv=ty)
        mc.setAttr(cNodeName + '.{}_init_translateY'.format(i), e=True, keyable=False, lock=True)
        mc.addAttr(cNodeName, ln='{}_init_translateZ'.format(i), at='float', dv=tz)
        mc.setAttr(cNodeName + '.{}_init_translateZ'.format(i), e=True, keyable=False, lock=True)
        mc.addAttr(cNodeName, ln='{}_init_rotateX'.format(i), at='float', dv=rx)
        mc.setAttr(cNodeName + '.{}_init_rotateX'.format(i), e=True, keyable=False, lock=True)
        mc.addAttr(cNodeName, ln='{}_init_rotateY'.format(i), at='float', dv=ry)
        mc.setAttr(cNodeName + '.{}_init_rotateY'.format(i), e=True, keyable=False, lock=True)
        mc.addAttr(cNodeName, ln='{}_init_rotateZ'.format(i), at='float', dv=rz)
        mc.setAttr(cNodeName + '.{}_init_rotateZ'.format(i), e=True, keyable=False, lock=True)
