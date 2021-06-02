# -*- coding: utf-8 -*-
"""
Created on Wed Jun 2 16:51:43 2021


@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-Depth of Field Calibration
"""

from __init__ import *

def ROI(img_gray,center_ROI,zoom_factor):
    
    print(zoom_factor)
    #size of matrix
    height,width=np.shape(img_gray)
    
    #Area ROI size
    height_ROI = int(height / zoom_factor)
    width_ROI = int(width / zoom_factor)
    
    #half size
    half_height_ROI = int(height_ROI / 2)
    half_width_ROI = int(width_ROI/ 2)

    #center index
    i_center=int(center_ROI[0])
    j_center=int(center_ROI[1])
    
    return img_gray[i_center-half_height_ROI:i_center+half_height_ROI,
                    j_center-half_width_ROI:j_center+half_width_ROI]

imgs_folder=r'E:\GitHub\KAMERAWERK\VCM-Dual\Material\Depth of Field Calibration\g=1500mm\Left'

list_depth=[]
list_focus_value=[]

depth_start=int(os.listdir(imgs_folder)[0].split('mm')[0])

#traverse all image
for this_img_name in os.listdir(imgs_folder):
    
    #image file name
    this_img_path=imgs_folder+'\\'+this_img_name
    
    this_img_bgr=cv2.imread(this_img_path)
    
    #convert rgb img to gray img
    this_img_gray=cv2.cvtColor(this_img_bgr,cv2.COLOR_BGR2GRAY)
    
    center_ROI=list(np.array(np.shape(this_img_gray))/2)

    #fetch depth information from image name
    this_depth=int(this_img_name.split('mm')[0])
    
    #calculate focus value of this image
    this_focus_value=C_F_V.FocusValue(ROI(this_img_gray,center_ROI,8*this_depth/depth_start),'Boccignone')
    
    #collect data of this round
    list_depth.append(this_depth)
    list_focus_value.append(this_focus_value)
    
plt.plot(list_depth,list_focus_value)
