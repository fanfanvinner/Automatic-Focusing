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
            
from configuration_parameter import MODE_INTERVAL,length_step,step_index

import matplotlib.pyplot as plt

import calculation_depth_of_field as C_D_O_F

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
     
        this_focused_depth=(k+1)*length_step*2
        this_rear_DoF=list_rear_DoF[k]
        this_front_DoF=list_front_DoF[k]

        plt.gca().add_patch(plt.Rectangle(
            (this_focused_depth-length_step, this_front_DoF),  # (x,y)矩形左下角
            width=length_step*2,  
            height=this_rear_DoF-this_front_DoF,
            color='grey', 
            alpha=0.5))
        
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
        plt.hlines(y=list_focused_depth[k],
                   xmin=this_focused_depth-length_step,
                   xmax=this_focused_depth+length_step,
                   color='olive',
                   linestyle='-')
        
    if MODE_INTERVAL=='equal':
    
        #define index to plot
        list_index=[len(list_focused_depth)-1-k*step_index for k in range(int(len(list_focused_depth))//step_index)]
        
        list_index.reverse()
        
        plt.gca().set_xticks([(this_index+1)*length_step*2 for this_index in list_index])
        plt.gca().set_xticklabels([str(int(list_focused_depth[this_index])) for this_index in list_index])
        
    #set ticks fonts
    plt.tick_params(labelsize=12)
    labels=plt.gca().get_xticklabels()+plt.gca().get_yticklabels()
    

    #label fonts
    [this_label.set_fontname('Times New Roman') for this_label in labels]
    
    plt.ylabel('Depth of Field (mm)',fontdict=label_prop)
    plt.xlabel('Focused Depth (mm)',fontdict=label_prop)