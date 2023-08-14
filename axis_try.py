# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 08:41:54 2023

@author: SUHUYINI
"""

import numpy as np

new_array = np.arange(12,29,2)
print(new_array)

new_array.resize(3,3)
print(new_array)

print(" ")

show = np.sum(new_array,axis= 0)
print(show)

print(" ")

show = np.sum(new_array,axis=1)
print(show)
