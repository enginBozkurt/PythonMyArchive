# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:42:03 2018

@author: Engin Bozkurt
"""

# Files
# iPython Writing a File

# # Open the text.txt we made earlier
my_file = open('text.txt')

# Readlines returns a list of the lines in the file.
my_file.readlines()

# Writing to a File

# By default, using the open() function will only allow us to read the file, 
# we need to pass the argument 'w' to write over the file. For example:
# Add a second argument to the function, 'w' which stands for write
 
my_file = open('text.txt', 'w')
 
# Write to the file
my_file.write('This is a new line')


# open a file, process its contents, and make sure to close it
# append a new line
with open("text.txt", "a") as my_file:
    my_file.write("\nThis is another new line")
    

# Read the file
for line in open('text.txt', 'r'):
    print(line)

# close the file
my_file.close()  
 
 
