# -*- coding: utf-8 -*-
import maya.cmds as mc

def setDefaultPose(atList=''):
    attrList = atList
    print attrList
    # sec = mc.ls(sl=True, type='transform')
    #
    # for i in sec:
    #     tx = mc.getAttr(i + '.init_translateX')
    #     ty = mc.getAttr(i + '.init_translateY')
    #     tz = mc.getAttr(i + '.init_translateZ')
    #     rx = mc.getAttr(i + '.init_rotateX')
    #     ry = mc.getAttr(i + '.init_rotateY')
    #     rz = mc.getAttr(i + '.init_rotateZ')
    #
    #     mc.setAttr(i + '.translateX', tx, e=True)
    #     mc.setAttr(i + '.translateY', ty, e=True)
    #     mc.setAttr(i + '.translateZ', tz, e=True)
    #     mc.setAttr(i + '.rotateX', rx, e=True)
    #     mc.setAttr(i + '.rotateY', ry, e=True)
    #     mc.setAttr(i + '.rotateZ', rz, e=True)
