# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:17:43 2018

@author: Engin Bozkurt
"""

# all() and any()
# all() and any() are built-in functions in Python that allow us to conveniently 
# check for boolean matching in an iterable. all() will return True if all elements in an iterable are True.

lst = [True,True,False,True]

all(lst)

# Returns False because not all elements are True.

any(lst)

# Returns true because at least one of the elements in the list is True.