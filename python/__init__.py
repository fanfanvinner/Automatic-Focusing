# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:17:21 2019

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: initialization script
"""

import sys,os
    
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\Module')
sys.path.append(os.getcwd()+'\\Object')
sys.path=list(set(sys.path))

from o_circle import circle

import operation_path as O_P
import operation_curve as O_C
import operation_import as O_I
import operation_export as O_E
import operation_visualization as O_V

import calculation_contrast as C_C
import calculation_histogram as C_H
import calculation_peak_search as C_P_S
import calculation_focus_value as C_F_V
import calculation_texture_feature as C_T_F
import calculation_depth_of_field as C_D_O_F
import calculation_numerical_analysis as C_N_A
import calculation_scene_discrimination as C_S_D

import experiment_parameter as E_P
import simulation_automatic_focusing as S_A_F

import numpy as np
import matplotlib.pyplot as plt

from configuration_font import title_prop

from configuration_parameter import g_min,g_max,f

import cv2

from configuration_font import legend_prop,label_prop,title_prop,sample_prop