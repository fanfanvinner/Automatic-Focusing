# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:04:34 2020

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: Module-parameter
"""

#basic parameters
ROI_weight_5_area=[0.14]*4
ROI_weight_5_area.insert(0,0.44)

ROI_weight_9_area=[0.1]*8
ROI_weight_9_area.insert(4,0.2)
            
#zoom factor of ROI
zoom_factor=16

#threshold of luminance to make sure AE frame
luminance_threshold=100

#pre_fix: same part of imgs name
# pre_fix='12M_0500mm_VCM_bottom'
# pre_fix='12M_0500mm_VCM_top'
# pre_fix='top_VCM_'
# pre_fix='poLight_test_'
# pre_fix='M_Cali_Near'
pre_fix='VCM_'

#marker size of focus value samples
size_marker=6