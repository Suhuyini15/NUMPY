# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:14:06 2023

@author: SUHUYINI
"""

import numpy as np
x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])


#DISPLAYS THE SUM OF ROWS
show = np.sum(x, axis=1)
print(show)

print("")

#DISPLAYS THE SUM OF COLUMNS
show = np.sum(x, axis=0)
print(show)
print("")
print("")
print("")


A =np.arange(5,85,3)
A.resize(2,3,4)
print(A)

print("")
print("")

#ADDS THE COLUMNS OF THE TWO ARRAYS TOGETHER
disp = np.sum(A, axis=0)
print(disp)

print("")
print("")
#ADDS THE COLUMNS OF THE ARRAYS INDIVIDUALLY
disp = np.sum(A, axis=1)
print(disp)

print("")
print("")

#DISPLAYS THE SUM OF THE ROWS OF THE ARRAYS INDIVIDUALLY
disp = np.sum(A, axis=2)
print(disp)

print("")
print("")

