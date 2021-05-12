# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:41:47 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: Module-visualization
"""

from configuration_font import legend_prop,\
                               text_prop,\
                               label_prop,\
                               title_prop,\
                               annotation_prop
                               
import matplotlib.pyplot as plt

import calculation_depth_of_field as C_D_O_F

length_step=5

def PlotDoFAndg1D(list_focused_depth):
    
    n_sample=len(list_focused_depth)
    
    
    #list of rear depth of field
    list_rear_DoF=[C_D_O_F.RearDoFDepthFromDepth(g) for g in list_focused_depth]
    
    #list of front depth of field
    list_front_DoF=[C_D_O_F.FrontDoFDepthFromDepth(g) for g in list_focused_depth]
    
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
                   ymin=-length_step,
                   ymax=+length_step,
                   color='maroon',
                   linestyle='-')
        
        #front DoF
        plt.vlines(x=this_front_DoF,
                   ymin=-length_step,
                   ymax=+length_step,
                   color='steelblue',
                   linestyle='-')
        
        #focused depth
        plt.vlines(x=this_focused_depth,
                   ymin=-length_step,
                   ymax=+length_step,
                   color='olive',
                   linestyle='-')
    
    plt.yticks([])
    
    #set ticks fonts
    plt.tick_params(labelsize=12)
    labels=plt.gca().get_xticklabels()+plt.gca().get_yticklabels()
    
    #label fonts
    [this_label.set_fontname('Times New Roman') for this_label in labels]
    
    plt.xlabel('Depth of Field (mm)',fontdict=label_prop)
    
    plt.ylim([-length_step*2,length_step*2])
    
def PlotDoFAndg2D(list_focused_depth):
    
    n_sample=len(list_focused_depth)
    
    #list of rear depth of field
    list_rear_DoF=[C_D_O_F.RearDoFDepthFromDepth(g) for g in list_focused_depth]
    
    #list of front depth of field
    list_front_DoF=[C_D_O_F.FrontDoFDepthFromDepth(g) for g in list_focused_depth]
    
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
                   xmin=this_focused_depth-length_step,
                   xmax=this_focused_depth+length_step,
                   color='maroon',
                   linestyle='-')
        
        #front DoF
        plt.hlines(y=this_front_DoF,
                   xmin=this_focused_depth-length_step,
                   xmax=this_focused_depth+length_step,
                   color='steelblue',
                   linestyle='-')
        
        #focused depth
        plt.hlines(y=this_focused_depth,
                   xmin=this_focused_depth-length_step,
                   xmax=this_focused_depth+length_step,
                   color='olive',
                   linestyle='-')
    
    #set ticks fonts
    plt.tick_params(labelsize=12)
    labels=plt.gca().get_xticklabels()+plt.gca().get_yticklabels()
    
    #label fonts
    [this_label.set_fontname('Times New Roman') for this_label in labels]
    
    plt.ylabel('Depth of Field (mm)',fontdict=label_prop)
    plt.xlabel('Focused Depth (mm)',fontdict=label_prop)