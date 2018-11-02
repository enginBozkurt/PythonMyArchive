# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:53:14 2018

@author: Engin Bozkurt
"""

# Statements and sets

# Sets are an unordered collection of unique elements.
# We can construct them by using the set() function.


# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(l)


# iterating through in a dictionary with for loop
d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(key)
    print(value)


# break, continue, pass
    
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x ==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue


# range()
# range() allows us to create a list of numbers ranging from a starting point up to an ending point. 
# We can also specify step size.

for num in range(10):
    print(num)

# define start and final values in range (default start is zero)

start = 1
stop = 20 
x = range(start,stop)

for num in range(start,stop):
    print(num)



# List Comprehensions

# List comprehensions allow us to build out lists using a different notation.
# You can think of it as essentially a one line for loop built inside of brackets. For a simple example:

# Grab every letter in string
lst1 = [x for x in 'word']
lst1

# Square numbers in range and turn into list
lst2 = [x**2 for x in range(0,11)]
lst2


# Check for even numbers in a range
lst3 = [x for x in range(11) if x % 2 == 0]
lst3

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]
fahrenheit


# We can also perform nested list comprehensions, for example:
lst = [ x**2 for x in [x**2 for x in range(11)]]
lst


# Exercise
# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of 
# five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz") 
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

[word[0] for word in st.split()]
