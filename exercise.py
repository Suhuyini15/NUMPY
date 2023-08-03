# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:51:21 2023

@author: SUHUYINI
"""

import numpy as np

first = np.arange(12)
first.resize((2,3))
print(first)

second = np.arange(1,30,2)
second.resize((3,5))
print(second)

print("")

product1 = np.matmul(first,second)
print(product1)

try :
    product2 = np.multiply(first,second)
    print(product2)

except ValueError as e:
    print("ERROR! ERROR!",e)