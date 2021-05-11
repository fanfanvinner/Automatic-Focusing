# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:55:32 2021

@author: Wei Huajing
@company: KAMERAWERK
@e-mail: jerryweihuajing@126.com

@title: Module-Calculation of DoF
"""

from configuration_parameter import F,f,u

#------------------------------------------------------------------------------
"""
Calculation of length of field front [mm]

Args:
    g: focused depth
    
Returns:
    front DoF length
"""
def FrontDoFLength(g):

    return F*u*g*(g-f)/(f*f+F*u*(g-f));
    
#------------------------------------------------------------------------------
"""
Calculation of length of field rear [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF length
"""
def RearDoFLength(g):
    
    return F*u*g*(g-f)/(f*f-F*u*(g-f));

#------------------------------------------------------------------------------
"""
Calculation of depth of field front [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF depth
"""
def FrontDoFDepth(g):

    return g-FrontDoFLength(g)

#------------------------------------------------------------------------------
"""
Calculation of depth of field rear [mm]

Args:
    g: focused depth
    
Returns:
    rear DoF depth
"""
def RearDoFDepth(g):
   
    return g+RearDoFLength(g)
