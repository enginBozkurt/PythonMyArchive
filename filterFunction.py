# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:57:17 2018

@author: Engin Bozkurt
"""

# filter()

# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, 
# for which the function returns True.
# The function filter(function(),list) needs a function as its first argument. The function needs to return a Boolean 
# value (either True or False). This function will be applied to every element of the iterable. 
# Only if the function returns True will the element of the iterable be included in the result.


#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True

lst =range(20)

result = [*filter(even_check,lst)]

print(result)

# filter() is more commonly used with lambda functions, this because we usually 
# use filter for a quick job where we don't want to write an entire function. 
# Lets repeat the example above using a lambda expression:

result2 = [*filter(lambda x: x%2==0,lst)]

print(result2)