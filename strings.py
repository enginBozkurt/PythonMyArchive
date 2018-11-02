# -*- coding: utf-8 -*-
"""
Strings

Created on Wed Oct 31 16:39:50 2018

@author: Engin Bozkurt
"""

s = "EnginBozkurt"

s

#from the6thelement to the end
s[5:] 


s

 #from the begining but the last letter
s[:-1]

# We can also use index and slice notation to grab elements of a sequence 
# by a specified step size (the default is 1). For instance we can use 
# two colons in a row and then a number specifying the frequency to grab elements.

 # Grab everything, but go in step sizes of 2
s[::2]

# We can use this to print a string backwards
s[::-1]

# concatenate strings
s1 = "Hello"
s2= "\n"
s3= "World"

result = s1 + s2 + s3

print(result)


# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
newstring = "HELLO WORLD SPLIT ME!"
newstring.split()

# Split by a specific element (doesn't include the element that was split on)
newstring.split("W")
