# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:19:57 2021

@author: Rajat
"""


counter_dict = {}
with open('namelist.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)