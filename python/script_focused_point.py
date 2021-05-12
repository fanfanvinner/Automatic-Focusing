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

# PlotDoFAndg1D(list_focused_depth)
# plt.title('Depth of Field (equal Interval)',fontdict=title_prop)

# O_V.PlotDoFAndg2D(list_focused_depth)
# plt.title('Depth of Field based on Focused Depth (equal Interval)',fontdict=title_prop)

'''unequal interval A'''
list_focused_depth=[]

#define max focused depth
g_max=n_sample*interval_g

#unequal interval to cover all depth
for g in range(1,g_max,interval_g):
    
    if list_focused_depth==[]:
        
        list_focused_depth.append(g)
        
    last_rear_DoF=C_D_O_F.RearDoFDepthFromDepth(list_focused_depth[-1])
    this_front_DoF=C_D_O_F.FrontDoFDepthFromDepth(g)
    
    if this_front_DoF>last_rear_DoF:
        
        list_focused_depth.append(g)
        
# O_V.PlotDoFAndg1D(list_focused_depth)
# plt.title('Depth of Field (unequal Interval)',fontdict=title_prop)

# O_V.PlotDoFAndg2D(list_focused_depth)
# plt.title('Depth of Field based on Focused Depth (unequal Interval A)',fontdict=title_prop)

g_min=100
g_max=2000

# '''unequal interval from near'''
# #list of focused depth
# list_focused_depth=[g_min]

# while (list_focused_depth[-1]<g_max):
    
#     list_focused_depth.append(C_D_O_F.DepthFromLastDepth(list_focused_depth[-1]))
    
# O_V.PlotDoFAndg2D(list_focused_depth)
# plt.title('Depth of Field based on Focused Depth (from near)',fontdict=title_prop)

'''unequal interval from far'''
#list of focused depth
list_focused_depth=[g_max]

while (list_focused_depth[-1]>g_min):
    
    list_focused_depth.append(C_D_O_F.DepthFromNextDepth(list_focused_depth[-1]))
    
O_V.PlotDoFAndg2D(list_focused_depth)
plt.title('Depth of Field based on Focused Depth (from near)',fontdict=title_prop)
