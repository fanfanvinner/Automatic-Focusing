# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:55:32 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: Module-Calculation of DoF
"""

from configuration_parameter import F,f,u,K_rear,K_front

#------------------------------------------------------------------------------
"""
Calculation of length of field front [mm]

Args:
    g: focused depth
    
Returns:
    front DoF length
"""
def FrontDoFLengthFromDepth(g):

    return F*u*g*(g-f)/(f*f+F*u*(g-f));
    
#------------------------------------------------------------------------------
"""
Calculation of length of field rear [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF length
"""
def RearDoFLengthFromDepth(g):
    
    return F*u*g*(g-f)/(f*f-F*u*(g-f));

#------------------------------------------------------------------------------
"""
Calculation of depth of field front [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF depth
"""
def FrontDoFDepthFromDepth(g):

    return g-FrontDoFLengthFromDepth(g)

#------------------------------------------------------------------------------
"""
Calculation of depth of field rear [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF depth
"""
def RearDoFDepthFromDepth(g):
   
    return g+RearDoFLengthFromDepth(g)

#------------------------------------------------------------------------------
"""
Calculation of focused depth from front DoF Depth[mm]

Args:
    g_front: front DoF 
    
Returns:
    focused depth
"""
def DepthFromFrontDoFDepth(g_front):
    
    return g_front*(f**2-F*u*f)/(f**2-F*u*g_front)
    
#------------------------------------------------------------------------------
"""
Calculation of focused depth from rear DoF Depth [mm]

Args:
    g_rear: rear DoF 
    
Returns:
    focused depth
"""
def DepthFromRearDoFDepth(g_rear):
    
    return g_rear*(f**2+F*u*f)/(f**2+F*u*g_rear)

#------------------------------------------------------------------------------
"""
Calculation of focused depth from last focused depth [mm]

Args:
    g_last: last focused depth  
    
Returns:
    focused depth
"""
def DepthFromLastDepth(g_last):
    
    g_rear=(1-K_rear)*RearDoFDepthFromDepth(g_last)+K_rear*g_last
    
    return DepthFromFrontDoFDepth(g_rear)

#------------------------------------------------------------------------------
"""
Calculation of focused depth from next focused depth [mm]

Args:
    g_next: next focused depth  
    
Returns:
    focused depth
"""
def DepthFromNextDepth(g_next):
    
    g_front=(1-K_front)*FrontDoFDepthFromDepth(g_next)+K_front*g_next
    
    return DepthFromRearDoFDepth(g_front)

#------------------------------------------------------------------------------
"""
Calculation of image distance from object depth [mm]

Args:
    g: object depth  
    
Returns:
    image distance
"""
def ImageDepth(g):
    
    return f*g/(g-f)