# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:50:07 2019

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-Automatic Focusing Simulation
"""

"""
demand:
    1 gif look like peak search ['JL method','Rule-based']
    2 optimized frames construction
"""

from __init__ import *

'''fixed plane AF'''
# imgs_folder=r'C:\Users\ASUS\Desktop\Experiment\poLight-Medium-Coarse\60mm'
# imgs_folder=r'C:\Users\ASUS\Desktop\Experiment\poLight-Medium-Fine\60mm'
# imgs_folder=r'C:\Users\ASUS\Desktop\Material\Screen\30cm-bright'

# C_P_S.PeakSearch(imgs_folder,'Boccignone','5-Area','Binary')

# contain coarse and fine
# S_A_F.AutoFocusAnimation(imgs_folder,'Boccignone','Center')

# total_folder=r'D:\Material\Plant'
# total_folder=r'C:\Users\ASUS\Desktop\Material\Grape'
# total_folder=r'C:\Users\ASUS\Desktop\Material\Plant'

# for this_peak_search_method in ['Binary','Global','Coarse2Fine'][-1:]:
    
#     for this_ROI_mode in ['5-Area','9-Area','Center'][-1:]:
        
#         for this_imgs_folder_name in os.listdir(total_folder):

#             this_imgs_folder=total_folder+'\\'+this_imgs_folder_name

#             C_P_S.PeakSearch(this_imgs_folder,'Boccignone',this_ROI_mode,this_peak_search_met hod)
            
#             # S_A_F.LensAnimation(this_imgs_folder,'Boccignone',this_ROI_mode,this_peak_search_method)
#             # S_A_F.FOVAnimation(this_imgs_folder,'Boccignone',this_ROI_mode,this_peak_search_method)

# l=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
# idx_peak=C_P_S.GlobalSearch(l)

# # fixed_imgs_folder=r'E:\GitHub\KAMERAWERK\VCM-Dual\Material\Focus Calibration-Fine\g=498mm'
# fixed_imgs_folder=r'E:\GitHub\KAMERAWERK\VCM-Dual\Material\Stereo Effect Experiment\20210422\g=100mm'
# fixed_imgs_folder_A=fixed_imgs_folder+'\\Left'
# fixed_imgs_folder_B=fixed_imgs_folder+'\\Right'

# C_P_S.PeakSearch(fixed_imgs_folder_A,'Boccignone','Center','Global')
# C_P_S.PeakSearch(fixed_imgs_folder_B,'Boccignone','Center','Global')

# '''dynamic depth focus calibration'''
# #%%
total_folder=r'E:\GitHub\KAMERAWERK\VCM-Dual\Material\Stereo Effect Experiment\20210425'

list_object_depth=[]
list_VCM_code_focused_left=[]
list_VCM_code_focused_right=[]

# # #%%
# # g=98

# # imgs_folder_A=total_folder+'\\g='+str(g)+'mm\\A'
# # imgs_folder_B=total_folder+'\\g='+str(g)+'mm\\B'

# # list_object_depth.append(g)

# # list_VCM_code_focused_A.append(C_P_S.PeakSearch(imgs_folder_A,'Boccignone','9-Area','Global'))
# # list_VCM_code_focused_B.append(C_P_S.PeakSearch(imgs_folder_B,'Boccignone','5-Area','Global'))

# #%%

#traverse all image series and calculate VCM code of focused image
for this_imgs_folder_name in os.listdir(total_folder):
    
    this_imgs_folder_left=total_folder+'\\'+this_imgs_folder_name+'\\Left'
    this_imgs_folder_right=total_folder+'\\'+this_imgs_folder_name+'\\Right'
    
    list_object_depth.append(int(this_imgs_folder_name.strip('g=').strip('mm')))
    
    list_VCM_code_focused_left.append(C_P_S.PeakSearch(this_imgs_folder_left,'Boccignone','Center-5-Partition','Global'))
    list_VCM_code_focused_right.append(C_P_S.PeakSearch(this_imgs_folder_right,'Boccignone','Center-5-Partition','Global'))

# import dill
# dill.dump_session('focus_calibration_'+total_folder.split('\\')[-1]+'.pkl')