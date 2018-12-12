#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:08:20 2018

@author: nenshu
"""

# The desired linear regression relationship is y = 0.23 * x + 40.0
# x is in the range of 100 to 600

import random

f = open("revenue_rdexpense.csv", "w")
f.write("Revenue(Million Dollars), R&D Expense(Million Dollars)\n")

for i in range(0, 100):
    x = 100.0 + i * 5
    y = 0.23 * x + 40.0
    r = random.randint(1,501)
    if i % 2 == 0:
        y *= (1+r/10000.00) 
    else:
        y *= (1-r/10000.00)
    s = str(x) + "," + str(round(y,4)) + "\n"
    f.write(s)
    
f.close()

