# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:10:31 2023

@author: SUHUYINI
"""

import numpy as np
favorite = np.arange(1,45,2)
favorite.resize((4,4))
print(favorite)

print(" ")

#[a:b]
#a = column or row of array to begin slicing from
#b = number of rows or columns to slice from a 
#when slicing an array the set befor the comma is for rows and behind the comma is for columns
selected = favorite[1:3,1:3]
print(selected)

print(" ")

print(favorite[0:2,2:3])