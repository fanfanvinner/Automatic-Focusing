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

'''unequal interval no coverage'''
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
# plt.title('Depth of Field based on Focused Depth (no coverage)',fontdict=title_prop)

# '''coverage from near'''
# #list of focused depth
# list_focused_depth=[g_min]

# while (list_focused_depth[-1]<g_max):
    
#     list_focused_depth.append(C_D_O_F.DepthFromLastDepth(list_focused_depth[-1]))
    
# O_V.PlotDoFAndg2D(list_focused_depth)
# plt.title('Depth of Field based on Focused Depth (coverage from near)',fontdict=title_prop)

# '''unequal interval from far'''
#list of focused depth
list_focused_depth=[g_max]

while (list_focused_depth[-1]>g_min):
    
    list_focused_depth.append(C_D_O_F.DepthFromNextDepth(list_focused_depth[-1]))

#reverse the list for better visualization    
list_focused_depth.reverse()

O_V.PlotDoFAndg2D(list_focused_depth)
plt.title('Depth of Field based on Focused Depth (coverage from far)',fontdict=title_prop)

#generate tuple list to contain focused depth and its DOF
list_focused_depth_DoF=[]

#from far to near
list_focused_depth.reverse()

for this_depth in list_focused_depth:
    
    this_rear_DoF=C_D_O_F.RearDoFDepthFromDepth(this_depth)
    this_front_DoF=C_D_O_F.FrontDoFDepthFromDepth(this_depth)
    
    list_focused_depth_DoF.append((this_depth,this_front_DoF,this_rear_DoF))
    
O_E.WriteTupleList2File(list_focused_depth_DoF,'../Outcome/focused point depth.txt')

list_g=[this_depth[0] for this_depth in list_focused_depth_DoF]
list_b=[C_D_O_F.ImageDepth(g) for g in list_g]
    
O_C.Curve(list_g,
          list_b,
          'maroon',
          'Image Distance',
          'Object Depth (mm)',
          'Image Distance (mm)',
          'Image Distance-Object Depth Curve of Focused Points',
          method_smoothing='optimized fitting')

O_C.Curve(list_g[1:],
          np.diff(list_b),
          'olive',
          'Differnece of Image Distance',
          'Differnece of Object Depth (mm)',
          'Image Distance (mm)',
          'Differnece of Image Distance-Object Depth Curve of Focused Points',
          method_smoothing='optimized fitting')

file=open('../Outcome/g_code_98_3998_A.txt')

lines=file.readlines()

map_g_code={}

for this_line in lines:
    
    list_str=this_line.split(',')
    map_g_code[int(list_str[0])]=int(list_str[1])
    
#focused VCM code and depth
list_code=[]
list_depth=[]

for this_g in list_g:
    
    this_depth=int(this_g) 
    
    if this_depth in list(map_g_code.keys()):
        
        list_depth.append(this_depth)
        list_code.append(map_g_code[this_depth])

O_C.Curve(list_depth,
          list_code,
          'maroon',
          'Focused VCM Code',
          'Object Depth (mm)',
          'Focused VCM Code (--)',
          'Focused VCM Code-Object Depth Curve of Focused Points',
          method_smoothing='optimized fitting')

O_C.Curve(list_depth[1:],
          np.diff(list_code),
          'olive',
          'Differnece of Focused VCM Code',
          'Object Depth (mm)',
          'Differnece of Focused VCM Code (--)',
          'Differnece of Focused VCM Code-Object Depth Curve of Focused Points',
          method_smoothing='optimized fitting')