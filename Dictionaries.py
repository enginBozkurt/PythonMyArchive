# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:19:03 2018

@author: Engin Bozkurt
"""
# Dictionaries 
# If you're familiar with other languages you can think of these Dictionaries as hash tables.
# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike 
# a sequence that stored objects by their relative position. This is an important distinction, 
# since mappings won't retain order since they have objects defined by a key.

# Constructing a Dictionary

# Make a dictionary with {} and : to signify a key and a value

my_dict = {'key1': 'value1', 'key2': 'value2'}

# Call values by their key
my_dict['key2']

# Its important to note that dictionaries are very flexible in the data types they can hold. For example:
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

#Lets call items from the dictionary
my_dict['key3']

# Can call an index on that value
my_dict['key3'][0]

# Can then even call methods on that value
my_dict['key3'][0].upper()

# We can effect the values of a key as well. For instance:
my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

#Check
my_dict['key1']

# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
my_dict['key1']

# We can also create keys by assignment. For instance if we started off with an empty dictionary, 
# we could continually add to it:

d = {}

d['animal'] = 'dog'
d['answer'] = '42'

#Show
d

# Nesting with Dictionaries
# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Let's see how we can grab that value:
# Keep calling the keys
d['key1']['nestkey']['subnestkey']

# A few Dictionary Methods

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
d.keys()

# # Method to grab all values
d.values()

# Method to return tuples of all items
d.items()
