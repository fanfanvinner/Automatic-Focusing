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

#FOV angle in 3 axis
angle_H=64.9
angle_V=51.2
angle_D=77.4

baseline=20

#Truly 12M
#pixel size [mm]
u = 1.4/1000;
#f number 
k = 1.8;
#focal length [mm]
f= 4.36;

#depth of field front [mm]
def FrontDepthOfField(g):

    return k*u*g*(g-f)/(f*f+k*u*(g-f));
    
#depth of field rear [mm]
def RearDepthOfField(g):

    return k*u*g*(g-f)/(f*f-k*u*(g-f));

def FrontPoint(g):
    
    return g-FrontDepthOfField(g)

def RearPoint(g):
    
    return g+RearDepthOfField(g)

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
    
g=600

DualFOV(g)

