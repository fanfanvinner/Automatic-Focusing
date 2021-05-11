# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:26:03 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-Focused Point based on DoF
"""

from __init__ import *

'''equal interval'''
n_sample=500
interval_g=5

#list of focused depth
list_focused_depth=[(k+1)*interval_g for k in range(n_sample)]

def PlotDoFAndg1D(list_focused_depth):
    
    n_sample=len(list_focused_depth)
    
    #list of rear depth of field
    list_rear_DoF=[C_D_O_F.RearDoFDepth(g) for g in list_focused_depth]
    
    #list of front depth of field
    list_front_DoF=[C_D_O_F.FrontDoFDepth(g) for g in list_focused_depth]
    
    plt.figure(figsize=(13,6))
    
    for k in range(n_sample):
     
        this_focused_depth=list_focused_depth[k]
        this_rear_DoF=list_rear_DoF[k]
        this_front_DoF=list_front_DoF[k]
        
        #DoF range
        plt.hlines(y=0,
                   xmin=this_rear_DoF,
                   xmax=this_front_DoF,
                   color='tan',
                   linestyle='-')
        
        #rear DoF
        plt.vlines(x=this_rear_DoF,
                   ymin=-interval_g/2,
                   ymax=+interval_g/2,
                   color='maroon',
                   linestyle='-')
        
        #front DoF
        plt.vlines(x=this_front_DoF,
                   ymin=-interval_g/2,
                   ymax=+interval_g/2,
                   color='steelblue',
                   linestyle='-')
        
        #focused depth
        plt.vlines(x=this_focused_depth,
                   ymin=-interval_g/2,
                   ymax=+interval_g/2,
                   color='olive',
                   linestyle='-')
    
    plt.yticks([])
    
    #set ticks fonts
    plt.tick_params(labelsize=12)
    labels=plt.gca().get_xticklabels()+plt.gca().get_yticklabels()
    
    #label fonts
    [this_label.set_fontname('Times New Roman') for this_label in labels]
    
    plt.xlabel('Depth of Field (mm)',fontdict=label_prop)
    
    plt.ylim([-interval_g*3,interval_g*3])
    
def PlotDoFAndg2D(list_focused_depth):
    
    n_sample=len(list_focused_depth)
    
    #list of rear depth of field
    list_rear_DoF=[C_D_O_F.RearDoFDepth(g) for g in list_focused_depth]
    
    #list of front depth of field
    list_front_DoF=[C_D_O_F.FrontDoFDepth(g) for g in list_focused_depth]
    
    plt.figure(figsize=(13,6))
    
    for k in range(n_sample):
     
        this_focused_depth=list_focused_depth[k]
        this_rear_DoF=list_rear_DoF[k]
        this_front_DoF=list_front_DoF[k]
        
        #DoF range
        plt.vlines(x=this_focused_depth,
                   ymin=this_rear_DoF,
                   ymax=this_front_DoF,
                   color='tan',
                   linestyle='-')
        
        #rear DoF
        plt.hlines(y=this_rear_DoF,
                   xmin=this_focused_depth-interval_g/2,
                   xmax=this_focused_depth+interval_g/2,
                   color='maroon',
                   linestyle='-')
        
        #front DoF
        plt.hlines(y=this_front_DoF,
                   xmin=this_focused_depth-interval_g/2,
                   xmax=this_focused_depth+interval_g/2,
                   color='steelblue',
                   linestyle='-')
        
        #focused depth
        plt.hlines(y=this_focused_depth,
                   xmin=this_focused_depth-interval_g/2,
                   xmax=this_focused_depth+interval_g/2,
                   color='olive',
                   linestyle='-')
    
    #set ticks fonts
    plt.tick_params(labelsize=12)
    labels=plt.gca().get_xticklabels()+plt.gca().get_yticklabels()
    
    #label fonts
    [this_label.set_fontname('Times New Roman') for this_label in labels]
    
    plt.ylabel('Depth of Field (mm)',fontdict=label_prop)
    plt.xlabel('Focused Depth (mm)',fontdict=label_prop)
    
# PlotDoFAndg1D(list_focused_depth)
# plt.title('Depth of Field (equal Interval)',fontdict=title_prop)

PlotDoFAndg2D(list_focused_depth)
plt.title('Depth of Field based on Focused Depth (equal Interval)',fontdict=title_prop)

'''unequal interval A'''
list_focused_depth=[]

#define max focused depth
g_max=n_sample*interval_g

#unequal interval to cover all depth
for g in range(1,g_max,interval_g):
    
    if list_focused_depth==[]:
        
        list_focused_depth.append(g)
        
    last_rear_DoF=C_D_O_F.RearDoFDepth(list_focused_depth[-1])
    this_front_DoF=C_D_O_F.FrontDoFDepth(g)
    
    if this_front_DoF>last_rear_DoF:
        
        list_focused_depth.append(g)
        
PlotDoFAndg1D(list_focused_depth)
plt.title('Depth of Field (unequal Interval)',fontdict=title_prop)

PlotDoFAndg2D(list_focused_depth)
plt.title('Depth of Field based on Focused Depth (unequal Interval A)',fontdict=title_prop)

'''unequal interval A'''
