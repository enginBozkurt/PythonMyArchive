# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:10:51 2018

@author: Engin Bozkurt
"""

# map()

# map() is a function that takes in two arguments: a function and a sequence iterable. 
# In the form: map(function, sequence)
# The first argument is the name of a function and the second a sequence (e.g. a list). map() 
# applies the function to all the elements of the sequence. It returns a new list 
# with the elements changed by function.

# We'll start with two functions:

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
    
temp = [0, 22.5, 40,100]

# Now lets see map() in action:
F_temps = [*map(fahrenheit, temp)] # Unpacking Generalizations

#Show
F_temps

# Convert back
[*map(celsius, F_temps)]

# In the example above we haven't used a lambda expression. By using lambda, 
# we wouldn't have had to define and name the functions fahrenheit() and celsius().
[*map(lambda x: (5.0/9)*(x - 32), F_temps)]


# map() can be applied to more than one iterable. The iterables have to have the same length.

# For instance, if we are working with two lists-map() will apply its lambda function to the elements of 
# the argument lists, i.e. it first applies to the elements with the 0th index, 
# then to the elements with the 1st index until the n-th index is reached.

# For example lets map a lambda expression to two lists:

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

[*map(lambda x,y:x+y, a,b)]

# Now all three lists
[*map(lambda x,y,z:x+y+z, a,b,c)]

# We can see in the example above that the parameter x gets its values from the list a, 
# while y gets its values from b and z from list c.
