# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:55:12 2018

@author: Engin Bozkurt
"""

# Iterators and Generators

# In this section of the course we will be learning about the difference 
# between iteration and generation in Python and how to construct our own 
# Generators with the yield statement. Generators allow us to generate as 
# we go along, instead of holding everything in memory.

# Generator functions allow us to write a function that can send back a value 
# and then later resume to pick up where it left off.

# This type of function is a generator in Python, allowing us to generate a 
# sequence of values over time. The main difference in syntax will be the use of 
# a yield statement.

# In most aspects, a generator function will appear very similar to a normal function. 
# The main difference is when a generator function is compiled they become an 
# object that support an iteration protocol. That means when they are called 
# in your code the don't actually return a value and then exit, the generator 
# functions will automatically suspend and resume their execution and state around the 
# last point of value generation. The main advantage here is that instead of having to 
# compute an entire series of values upfront and the generator functions can be suspended, 
# this feature is known as state suspension.

# Generators are best for calculating large sets of results (particularly in calculations 
# that involve loops themselves) in cases where we don’t want to allocate the memory for 
# all of the results at the same time.


# Lets create an example generator which calculates fibonacci numbers:
def genfibon(n):
    
    a = 0
    b = 1
    
    for i in range(n):
        yield b
        t = a
        a = b
        b = b+t

# test
for num in genfibon(10):
    print(num)
    
for num in genfibon(100):
    print(num)


# next() and iter() built-in functions
    
# A key to fully understanding generators is the next function() and the iter() function.
# The next function allows us to access the next element in a sequence. Lets check it out:

def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen 
g = simple_gen()

print(next(g))  # output is 0
    
print(next(g)) # output is 1

print(next(g)) # output is 2


# After yielding all the values next() caused a StopIteration error. 
# What this error informs us of is that all the values have been yielded.

# You might be wondering that why don’t we get this error while using a for loop? 
# The for loop automatically catches this error and stops calling next.

# Lets go ahead and check out how to use iter(). You remember that strings are iterables:

s = 'hello'

#Iterate over string
for let in s:
    print(let)


# But that doesn't mean the string itself is an iterator! We can check this with the next() function:

# Interesting, this means that a string object supports iteration, 
# but we can not directly iterate over it as we could with a generator function.
# The iter() function allows us to do just that!

s_iter = iter(s)

next(s_iter) # output is 'h'

next(s_iter) # output is 'e'
