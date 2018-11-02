# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:15:18 2018

@author: Engin Bozkurt
"""

# class
# The class is a blueprint that defines a nature of a future object. 
# From classes we can construct instances.
# The class is a blueprint that defines a nature of a future object.
# From classes we can construct instances. An instance is a specific object created from a particular class.

# # Create a new object type called Sample
class Sample(object):
    pass

# Instance of Sample
x = Sample()


print(type(x))

# An attribute is a characteristic of an object. A method is an operation we can perform with the object.
# For example we can create a class called Dog. An attribute of a dog may be its breed or its name,
# while a method of a dog may be defined by a .bark() method which returns a sound.

# Attributes

# The syntax for creating an attribute is:

# self.attribute = something

# There is a special method called: __init__() is called automatically right after the object has been created.

# def __init__(self, breed):

# Each attribute in a class definition begins with a reference to the instance object. 
# It is by convention named self. The breed is the argument. The value is passed during the class instantiation.

# This method is used to initialize the attributes of an object. For example:

# In Python there are also class object attributes. These Class Object Attributes 
# are the same for any instance of the class.

# Note that the Class Object Attribute is defined outside of any methods in the class. 
# Also by convention, we place them first before the init.

class Dog(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
# create an instance from class and retrieve its attributes
sam = Dog('Lab','Sam')
        
sam.breed
sam.name


# Methods 
# Methods are functions defined inside the body of a class. 
# They are used to perform operations with the attributes of our objects. 
# Methods are essential in encapsulation concept of the OOP paradigm. 
# This is essential in dividing responsibilities in programming, especially in large applications.


class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1) (initializer method)
    def __init__(self, radius=1):
        self.radius = radius 

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius
   
# test
c = Circle()

c.setRadius(2)
print('Radius is: ',c.getRadius())
print('Area is: ',c.area())


# Special Methods

class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    
    #method is to create a string representation of the object
    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)
    
    # length method 
    # The __len__ method is the implementation of len() public interface
    def __len__(self):
        return self.pages
    
    #destructor method
    def __del__(self):
        print("A book is destroyed")

# test
book = Book("Python Rocks!", "Jose Portilla", 159) 

#Special Methods
print(book)
print(len(book))
del(book)       
