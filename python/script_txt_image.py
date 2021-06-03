# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:32:19 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: script-read txt image
"""

from __init__ import *

data_real_time=np.loadtxt(r'E:\GitHub\KAMERAWERK\VCM-Dual\Outcome\gray-real-time.txt').astype(np.uint8)
data_off_line=np.loadtxt(r'E:\GitHub\KAMERAWERK\Automatic-Focusing\Outcome\gray-off-line.txt').astype(np.uint8)

plt.figure()
plt.imshow(data_real_time,cmap='gray')

plt.figure()
plt.imshow(data_off_line,cmap='gray')

height=data_real_time.shape[0]
width=data_real_time.shape[1]

a=C_C.GlobalContrast(data_real_time[int(height/2-height/16):int(height/2+height/16),
                                    int(width/2-width/16):int(width/2+width/16)],
                     'Boccignone')

b=C_C.GlobalContrast(data_real_time[int(height/2-height/16):int(height/2+height/16),
                                    int(width/2-width/16):int(width/2+width/16)],
                     'Boccignone')