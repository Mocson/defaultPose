# -*- coding: utf-8 -*-

import maya.cmds as mc

def saveDefaultPose():
    sec = mc.ls(sl=True, type='transform')

    for i in sec:
        tx = mc.getAttr(i + '.translateX')
        ty = mc.getAttr(i + '.translateY')
        tz = mc.getAttr(i + '.translateZ')
        rx = mc.getAttr(i + '.rotateX')
        ry = mc.getAttr(i + '.rotateY')
        rz = mc.getAttr(i + '.rotateZ')

        mc.addAttr(i, ln='init_translateX', at='float', dv=tx)
        mc.setAttr(i + '.init_translateX', e=True, keyable=False, lock=True)
        mc.addAttr(i, ln='init_translateY', at='float', dv=ty)
        mc.setAttr(i + '.init_translateY', e=True, keyable=False, lock=True)
        mc.addAttr(i, ln='init_translateZ', at='float', dv=tz)
        mc.setAttr(i + '.init_translateZ', e=True, keyable=False, lock=True)
        mc.addAttr(i, ln='init_rotateX', at='float', dv=rx)
        mc.setAttr(i + '.init_rotateX', e=True, keyable=False, lock=True)
        mc.addAttr(i, ln='init_rotateY', at='float', dv=ry)
        mc.setAttr(i + '.init_rotateY', e=True, keyable=False, lock=True)
        mc.addAttr(i, ln='init_rotateZ', at='float', dv=rz)
        mc.setAttr(i + '.init_rotateZ', e=True, keyable=False, lock=True)

def setDefaultPose():
    sec = mc.ls(sl=True, type='transform')

    for i in sec:
        tx = mc.getAttr(i + '.init_translateX')
        ty = mc.getAttr(i + '.init_translateY')
        tz = mc.getAttr(i + '.init_translateZ')
        rx = mc.getAttr(i + '.init_rotateX')
        ry = mc.getAttr(i + '.init_rotateY')
        rz = mc.getAttr(i + '.init_rotateZ')

        mc.setAttr(i + '.translateX', tx, e=True)
        mc.setAttr(i + '.translateY', ty, e=True)
        mc.setAttr(i + '.translateZ', tz, e=True)
        mc.setAttr(i + '.rotateX', rx, e=True)
        mc.setAttr(i + '.rotateY', ry, e=True)
        mc.setAttr(i + '.rotateZ', rz, e=True)
