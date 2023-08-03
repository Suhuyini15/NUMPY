# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:33:42 2023

@author: SUHUYINI
"""

import numpy as np

#matrix of only one
first = np.ones((2,2))
print(first)

print("")

#matrix of only zeros
zero = np.zeros((3,3))
print(zero)

print("")

#2x2 matrix where 3,7 are placed diagonally
diagonal = np.diag([3,7])
print(diagonal)

print("")

#scalar multipliers and additions affect individually every number in the matrix
# addition of matrix is possible when both have the same size
total = 2*first + 4*diagonal + 3
print(total)
                     
                    