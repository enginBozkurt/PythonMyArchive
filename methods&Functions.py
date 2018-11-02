# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:39:57 2018

@author: Engin Bozkurt
"""

# the function finds whether a number is prime 

import math

def is_prime(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# test is_prime function
is_prime(16)
is_prime(71)


# lambda expressions

# Lambda's body is a single expression, not a block of statements.
# Lambda expressions allow us to create "anonymous" functions. This basically 
# means we can quickly make ad-hoc functions without needing to properly define 
# a function using def.
# The lambda's body is similar to what we would put in a def body's return statement.

square = lambda num: num**2

square(2)

# Check it a number is even
even = lambda x: x%2==0
even(16)

# Grab first character of a string:
first = lambda s: s[0]
first('engin')

# Reverse a string:
rev = lambda s: s[::-1]
rev('engin')

# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam or nurses run.

def palindrome(s):
    s = s.replace(' ','') # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1] # Check through slicing

palindrome('abcba')
