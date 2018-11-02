# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:50:29 2018

@author: Engin Bozkurt
"""

# zip
# zip() makes an iterator that aggregates elements from each of the iterables.
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from 
# each of the argument sequences or iterables. 
# The iterator stops when the shortest input iterable is exhausted.

# zip() should only be used with unequal length inputs when you don’t care about trailing, 
# unmatched values from the longer iterables.
# Lets see it in action in some examples:

x = [1,2,3]
y = [4,5,6]

# Zip the lists together
result = [*zip(x,y)]

print(result)

# Note how tuples are returned. What if one iterable is longer than the other?
x2 = [1,2,3]
y2 = [4,5,6,7,8]

# Zip the lists together
result2 = [*zip(x2,y2)]
print(result2)

# Note how the zip is defined by the shortest iterable length. Its generally 
# advised not to zip unequal length iterables unless your very sure you only need partial tuple pairings.
# What happens if we try to zip together dictionaries?

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

result3 = [*zip(d1,d2)]
print(result3)

# This makes sense because simply iterating through the dictionaries will result 
# in just the keys. We would have to call methods to mix keys and values:

result4 = [*zip(d2,d1.values())]
print(result4)


# Finally lets use zip a to switch the keys and values of the two dictionaries:
def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key] = d2val
    
    return dout

# test
switcharoo(d1,d2)