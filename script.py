# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:50:07 2019

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title：Contrast Calculation
"""

from __init__ import *

import os
import cv2

import copy as cp
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import FontProperties

#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Distance\Invarious\Coarse'
#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Distance\Various\Coarse'
#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Luminance\High\Coarse'
#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Luminance\Low\Coarse'
#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Texture\Obvious\Coarse'
#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Texture\Unobvious\Coarse'

#img_gray=Im.BatchImport(imgs_folder)[1][10]
#plt.imshow(img_gray,cmap='gray')
#cv2.imshow('gray',img_gray)

#folder_total=r'C:\Users\Administrator\Desktop\Experiment'
#
#for name_this_experiment in os.listdir(folder_total):
#    
#    E_P.ExperimentContrastComparison(folder_total+'\\'+name_this_experiment,'Constant')
#    E_P.ExperimentContrastComparison(folder_total+'\\'+name_this_experiment,'Advanced')

#imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Texture\Unobvious' 
imgs_folder=r'C:\Users\Administrator\Desktop\Experiment\Texture\Obvious' 

def ExperimentOperator(imgs_folder):
    
    print('')
    print('-- Experiment Operator')
    
    list_contrast_operator=['KK',
                            'Whittle',
                            'Burkhardt',
                            'Michelson',
                            'Peli',
                            'WSC',
                            'Weber',
                            'Stevens',
                            'Boccignone',
                            'SD',
                            'SDLG',
                            'SAM',
                            'SALGM',
                            'SAW',
                            'SALGW']
    
    for this_contrast_operator in list_contrast_operator:
       
        S_A_F.ImageAndContrast(imgs_folder,this_contrast_operator)
        
ExperimentOperator(imgs_folder) 
   
'''criteria of Critiria and Algorithm from DB or photos''' 
'''optimized frames construction'''
