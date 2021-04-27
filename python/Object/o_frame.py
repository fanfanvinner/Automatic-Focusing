# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:03:19 2019

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title：Object-frame
"""

import cv2
import numpy as np

import calculation_focus_value as C_F_V

from configuration_parameter import zoom_factor,\
                                    ROI_weight_5_area,\
                                    ROI_weight_9_area

#==============================================================================
#object to operate image
#============================================================================== 
class frame:
    def __init__(self,
                 path=None,
                 pre_fix=None,
                 img_bgr=None,
                 img_gray=None,
                 img_ROI=None,
                 focus_value=None,
                 lens_position_code=None):
        self.path=path
        self.pre_fix=pre_fix
        self.img_bgr=img_bgr
        self.img_gray=img_gray
        self.img_ROI=img_ROI
        self.focus_value=focus_value
        self.lens_position_code=lens_position_code
        
    def Init(self,operator,ROI_mode,flag_plot=False):
        
        #read image
        self.img_bgr=cv2.imread(self.path)
        
        #convert rgb img to gray img
        self.img_gray=cv2.cvtColor(self.img_bgr,cv2.COLOR_BGR2GRAY)
        
        #VCM code calculation
        try:
            
            self.lens_position_code=int(self.path.strip('.jpg').split(self.pre_fix)[-1])
            
        except:
            
            if self.pre_fix!='':
     
                self.lens_position_code=int(self.path.strip('.png').split(self.pre_fix)[-1])
            
            else:
                
                self.lens_position_code=int(self.path.split('\\')[-1].strip('.png'))
                                            
        #size of img
        height,width=np.shape(self.img_gray)

        ROI_linewidth=int(height//300)
        
        #image of ROI
        self.img_ROI=np.full(np.shape(self.img_gray),np.nan)
        
        #size of area
        area_half_height=int(np.shape(self.img_gray)[0]/zoom_factor)
        area_half_width=int(np.shape(self.img_gray)[1]/zoom_factor)
 
        if ROI_mode=='9-Area':
            
            list_center_9_area=[[height/2+i*height/4,width/2+j*width/4] for i in [-1,0,1] for j in [-1,0,1]]
            
            #calculate contrast in each area
            list_contrast_9_areas=[]
            
            for i_a,j_a in list_center_9_area:
                        
                this_area=self.img_gray[int(i_a)-area_half_height:int(i_a)+area_half_height,
                                        int(j_a)-area_half_width:int(j_a)+area_half_width]
            
                #collect it
                list_contrast_9_areas.append(C_F_V.FocusValue(this_area,operator))
            
                #draw the bound of ROI
                for k_a in range(ROI_linewidth):
                    
                    '''NEED MODIFICATION'''
                    self.img_ROI[int(i_a-k_a)-area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                    self.img_ROI[int(i_a+k_a)+area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                    self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a-k_a)-area_half_width]=1
                    self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a+k_a)+area_half_width]=1
            
            #collect the data
            self.focus_value=np.sum(np.array(ROI_weight_9_area)*np.array(list_contrast_9_areas))
       
        elif ROI_mode=='5-Area':
            
            list_center_5_area=[[ height/2, width/2],
                                [ height/4, width/4],
                                [ height/4,-width/4],
                                [-height/4,-width/4],
                                [-height/4, width/4]]
            
            #calculate contrast in each area
            list_contrast_5_area=[]
            
            for i_a,j_a in list_center_5_area:
                        
                this_area=self.img_gray[int(i_a)-area_half_height:int(i_a)+area_half_height,
                                        int(j_a)-area_half_width:int(j_a)+area_half_width]
            
                #collect it
                list_contrast_5_area.append(C_F_V.FocusValue(this_area,operator))
            
                #draw the bound of ROI
                for k_a in range(ROI_linewidth):
                    
                    self.img_ROI[int(i_a-k_a)-area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                    self.img_ROI[int(i_a+k_a)+area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                    self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a-k_a)-area_half_width]=1
                    self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a+k_a)+area_half_width]=1
            
            #collect the data
            self.focus_value=np.sum(np.array(ROI_weight_5_area)*np.array(list_contrast_5_area))
       
        elif ROI_mode=='Center':
            
            i_a,j_a=height/2, width/2
                        
            this_area=self.img_gray[int(i_a)-area_half_height:int(i_a)+area_half_height,
                                    int(j_a)-area_half_width:int(j_a)+area_half_width]
        
            #collect the data
            self.focus_value=C_F_V.FocusValue(this_area,operator)
        
            #draw the bound of ROI
            for k in range(ROI_linewidth):
                
                self.img_ROI[int(i_a-k_a)-area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                self.img_ROI[int(i_a+k_a)+area_half_height,int(j_a-k_a)-area_half_width:int(j_a+k_a+1)+area_half_width]=1
                self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a-k_a)-area_half_width]=1
                self.img_ROI[int(i_a-k_a)-area_half_height:int(i_a+k_a+1)+area_half_height,int(j_a+k_a)+area_half_width]=1
      
        elif ROI_mode=='Center-5-Partition':
            
            i_a,j_a=height/2, width/2
            
            #size of center ROI
            width_ROI=area_half_width*2
            height_ROI=area_half_height*2
            
            #size of partition of ROI
            partition_half_width=int(width_ROI/zoom_factor)
            partition_half_height=int(width_ROI/zoom_factor)
            
            list_center_5_partition=[[ 0, 0],
                                     [ height_ROI/4, width_ROI/4],
                                     [ height_ROI/4,-width_ROI/4],
                                     [-height_ROI/4,-width_ROI/4],
                                     [-height_ROI/4, width_ROI/4]]
            
            #calculate contrast in each area
            list_contrast_5_partition=[]
            
            for i_p,j_p in list_center_5_partition:
                        
                this_partition=self.img_gray[int(i_a+i_p)-partition_half_height:int(j_a+j_p)+partition_half_height,
                                             int(i_a+i_p)-partition_half_width:int(j_a+j_p)+partition_half_width]
            
                #collect it
                list_contrast_5_partition.append(C_F_V.FocusValue(this_partition,operator))
            
                #draw the bound of ROI
                for k_p in range(ROI_linewidth):
                    
                    self.img_ROI[int(i_a+i_p-k_p)-partition_half_height,
                                 int(j_a+j_p-k_p)-partition_half_width:int(j_a+j_p+k_p+1)+partition_half_width]=1
                   
                    self.img_ROI[int(i_a+i_p+k_p)+partition_half_height,
                                 int(j_a+j_p-k_p)-partition_half_width:int(j_a+j_p+k_p+1)+partition_half_width]=1
                    
                    self.img_ROI[int(i_a+i_p-k_p)-partition_half_height:int(i_a+i_p+k_p+1)+partition_half_height,
                                 int(j_a+j_p-k_p)-partition_half_width]=1
                    
                    self.img_ROI[int(i_a+i_p-k_p)-partition_half_height:int(i_a+i_p+k_p+1)+partition_half_height,
                                 int(j_a+j_p+k_p)+partition_half_width]=1
            
            #collect the data
            self.focus_value=np.sum(np.array(ROI_weight_5_area)*np.array(list_contrast_5_partition))
        
        print('--> Lens Position Code:',self.lens_position_code)
        # print('--> Focus Value:',self.focus_value)
        
        if not flag_plot:
            
            #release the storage
            self.img_bgr=None
            self.img_gray=None
            self.img_ROI=None