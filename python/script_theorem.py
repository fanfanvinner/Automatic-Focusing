# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:50:07 2019

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-theoretical derivation of VCM Code and Depth
"""

v_0=10
K=0.001
f=6

def Depth(VCM):
    
    v=v_0-VCM*K
    
    return v*f/(v-f)


import numpy as np

list_depth=[]
list_VCM=[]

for k in range(300,800):
    
    list_VCM.append(k)
    list_depth.append(Depth(k))
    
import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(list_depth,list_VCM)


def u(v):
    
    return v*f/(v-f)

list_u=[]
list_v=[]

for kk in range(300,800):
    
    list_u.append(u(kk))
    list_v.append(kk)
    
plt.figure(2)
plt.plot(list_u,list_v)