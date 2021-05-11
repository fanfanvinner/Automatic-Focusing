# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:12:34 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-Automatic Focusing Simulation
"""

import numpy as np

def LengthFromAngle(angle,depth):
    
    return 2*depth*np.tan(np.pi/180*angle/2)

def SlopeLenth(length_horizontal,length_vertical):
    
    return np.sqrt(length_horizontal**2+length_vertical**2)

def DualFOV(g):
    
    length_H=LengthFromAngle(angle_H,g)
    length_V=LengthFromAngle(angle_V,g)
    # length_D=LengthFromAngle(angle_D,g)
    # ratio=length_V/length_H

    # length_D_calculated=SlopeLenth(length_H,length_V)
    
    length_H_dual=length_H-baseline
    
    print('')
    print('==> Horizontal Size: %d [mm]'%length_H_dual)
    print('==> Vertical Size: %d [mm]'%length_V)
    print('==> Rear Depth of Field: %d [mm]'%RearDepthOfField(g))
    print('==> Front Depth of Field: %d [mm]'%FrontDepthOfField(g))
    print('==> Rear Point: %d [mm]'%RearPoint(g))
    print('==> Front Point: %d [mm]'%FrontPoint(g))
    
[DualFOV(g) for g in [200,300,400,500,600,700,800,1000,1200]]


