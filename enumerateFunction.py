# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:36:13 2018

@author: Engin Bozkurt
"""

# enumerate()
# In this lecture we will learn about an extremely useful built-in function: enumerate(). 
# Enumerate allows you to keep a count as you iterate through an object. 
# It does this by returning a tuple in the form (count,element). 

list = ['a','b','c']

for number,item in enumerate(list):
    print(number)
    print(item)
    

# enumerate() becomes particularly useful when you have a case where you need to have some sort of tracker.
# For example:

for count,item in enumerate(list):
    if count >= 2:
        break
    else:
        print(item)