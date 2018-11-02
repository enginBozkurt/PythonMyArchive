# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:19:02 2018

@author: Engin Bozkurt
"""

# Tuples
# In Python tuples are very similar to lists, however, unlike lists they are immutable meaning 
# they can not be changed. You would use tuples to present things that shouldn't be changed, 
# such as days of the week, or dates on a calendar.

# You'll have an intuition of how to use tuples based on what you've learned about lists. 
# We can treat them very similarly with the major distinction being that tuples are immutable.

# Can create a tuple with mixed types
t = (1,2,3)

# Check len just like a list
len(t)

# Can also mix object types
t = ('one',2,[4,5,6])
t

# Use indexing just like we did in lists
t[0]

# Slicing just like a list
t[1:]

# Use .index to enter a value and return the index
t.index(2)

# Use .count to count the number of times a value appears
t.count('one')

# When to use Tuples
# You may be wondering, "Why bother using tuples when they have fewer available methods?" 
# To be honest, tuples are not used as often as lists in programming, but are used when 
# immutability is necessary. If in your program you are passing around an object and need 
# to make sure it does not get changed, then tuple become your solution. 
# It provides a convenient source of data integrity.