# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:47:20 2018

@author: LEngin Bozkurt
"""

# Unlike strings, Lists are mutable, meaning the elements inside a list can be changed!

# Assign a list to an variable named my_list
my_list = [1,2,3]

#We just created a list of integers, but lists can actually hold different object types. For example:
my_list = ['A string',23,100.232,'o']

# Just like strings, the len() function will tell you how many items are in the sequence of the list.

len(my_list)

# Grab index 1 and everything past it
newList = ['one','two','three',4,5]

newList[1:]

# Grab everything UP TO index 3
newList[:3]


# We can also use + to concatenate lists, just like we did for strings.
newList + ["new item"]

# Note: This doesn't actually change the original list!
newList

# You would have to reassign the list to make the change permanent.
newList = newList + ['add new list permanently']
print(newList)

# Basic List Methods

# Create a new list
l = [1,2,3]


# Append an element to the list
l.append('append me!')

# Show
l

# Use pop to "pop off" an item from the list. By default pop takes off the last index, 
# but you can also specify which index to pop off. 

# Pop off the 0 indexed item
l.pop(0)
l

# Assign the popped element, remember default popped index is -1
popped_item = l.pop()

popped_item


newList_2 = ['a', 'e', 'x', 'b', 'c']
# Use reverse to reverse order (this is permanent!)
newList_2.reverse()
newList_2

# Use sort to sort the list (in this case alphabetical order, but for numbers  it will go ascending)
newList_2.sort()
newList_2


# Nesting Lists
# A great feature of of Python data structures is that they support nesting. 
# This means we can have data structures within data structures. For example: 
# A list inside a list. Let's see how this works!


# Let's make three lists

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]


# Make a list of lists to form a matrix
matrix = [list_1,list_2,list_3]

# Grab first item in matrix object
matrix[0]

# Grab first item of the first item in the matrix object
matrix[0][0]


# List Comprehensions

# We used list comprehension here to grab the first element of every row in the matrix object.
first_col = [row[0] for row in matrix]

first_col


