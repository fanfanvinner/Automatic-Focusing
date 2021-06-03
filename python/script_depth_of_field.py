# -*- coding: utf-8 -*-
"""
Created on Wed Jun 2 16:51:43 2021


@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-Depth of Field Calibration
"""

from __init__ import *

def ROI(img_gray,center_ROI):
    
    zoom_factor=8
    
    #size of matrix
    height,width=np.shape(img_gray)[:2]
    
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

def DepthAndFocusValue(imgs_folder):
    
    list_depth=[]
    list_focus_value=[]
    list_ROI=[]
    
    #depth of nearest front DoF
    depth_start=int(os.listdir(imgs_folder)[0].split('mm')[0])
    
    #traverse all image
    for this_img_name in os.listdir(imgs_folder):
        
        #image file name
        this_img_path=imgs_folder+'\\'+this_img_name
        
        this_img_bgr=cv2.imread(this_img_path)
        
        #convert rgb img to gray and rgb img
        this_img_rgb=cv2.cvtColor(this_img_bgr,cv2.COLOR_BGR2RGB)
        this_img_gray=cv2.cvtColor(this_img_bgr,cv2.COLOR_BGR2GRAY)
        
        center_ROI=list(np.array(np.shape(this_img_gray))/2)
    
        #fetch depth information from image name
        this_depth=int(this_img_name.split('mm')[0])
        
        #calculate focus value of this image
        this_focus_value=C_F_V.FocusValue(ROI(this_img_gray,center_ROI),'Boccignone')
        
        #collect data of this round
        list_depth.append(this_depth)
        list_focus_value.append(this_focus_value)
        list_ROI.append(ROI(this_img_rgb,center_ROI))
    
    return list_depth,list_focus_value,list_ROI

def DisplayAndOutput(list_ROI,list_depth,imgs_folder):
        
    #rows and cols of image
    n_row=int(np.ceil(np.sqrt(9*len(list_depth)/16)))
    n_col=int(np.ceil(np.sqrt(16*len(list_depth)/9)))
    
    #image zoom factor
    zoom_factor=2.8
    
    plt.figure(figsize=(n_col*zoom_factor,n_row*zoom_factor))
    
    #generate output folder
    imgs_folder_output=imgs_folder.replace('Material','Outcome')
    
    O_P.GenerateFolder(imgs_folder_output)
    
    #traverse and plot subimage
    for k in range(len(list_ROI)):
        
        plt.subplot(n_row,n_col,k+1)
        
        plt.imshow(list_ROI[k])
        plt.xticks([])
        plt.yticks([])
        
        #title of this image
        this_title=str(list_depth[k])+'mm'
        
        plt.title(this_title,fontdict=title_prop)
        
        this_ROI_bgr=cv2.cvtColor(list_ROI[k],cv2.COLOR_RGB2BGR)
        cv2.imwrite(imgs_folder_output+'\\'+this_title+'.jpg',this_ROI_bgr)
        
imgs_folder=r'E:\GitHub\KAMERAWERK\VCM-Dual\Material\Depth of Field Calibration\Ideal\g=1000mm'

#imgs folder of left and right
imgs_folder_left=imgs_folder+'\\Left'
imgs_folder_right=imgs_folder+'\\Right'

#calculate relationship between depth and focus value
list_depth_left,\
list_focus_value_left,\
list_ROI_left=DepthAndFocusValue(imgs_folder_left)

list_depth_right,\
list_focus_value_right,\
list_ROI_right=DepthAndFocusValue(imgs_folder_right)

plt.figure(figsize=(13,6))

plt.plot(list_depth_left,list_focus_value_left,'-',color='maroon',label='Left Camera')
plt.plot(list_depth_left,list_focus_value_left,'o',color='k')
plt.plot(list_depth_right,list_focus_value_right,'-',color='olive',label='Right Camera')
plt.plot(list_depth_right,list_focus_value_right,'o',color='k')

plt.legend(prop=legend_prop,loc='lower right')  

ax=plt.gca()

#set ticks fonts
plt.tick_params(labelsize=12)
labels=ax.get_xticklabels()+ax.get_yticklabels()

#label fonts
[this_label.set_fontname('Times New Roman') for this_label in labels]
    
plt.title('Focus Value-Object Depth Curve from the same VCM code',fontdict=title_prop)

plt.xlabel('Object Depth (mm)',fontdict=label_prop)
plt.ylabel('Focus Value (--)',fontdict=label_prop)
 
plt.savefig(imgs_folder.replace('Material','Outcome')+'\\Curve.png',dpi=300,bbox_inches='tight')

#display and output ROI as several sub images
DisplayAndOutput(list_ROI_left,
                 list_depth_left,
                 imgs_folder_left)

DisplayAndOutput(list_ROI_right,
                 list_depth_right,
                 imgs_folder_right)