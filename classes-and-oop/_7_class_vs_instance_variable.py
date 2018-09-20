#!/usr/bin/python

'''
Class Variables
----------------
declared inside the class definition (but outside of any instance methods). They are not tie to any particular instance of a class.
Instead, class variables store their contents on the class itself, and all objects created from a particlar class share access to
the same set of class variables. This means for examples that modifying a class vairable affects all object instances at the same time.

Instance Variables
-------------------
always tied to a particular object instance. Their contents are not stored on the class, but on each individual object instance.
Their contents are not stored on the class, but on each individual object created from the class. Therefore, the contents of an instance
variable are completely independent from one object instance to the next. and so, modifying an instance variable only affects one object
instance at a time.

'''

class Dog:
    num_legs = 4 # <-- class Variables

    def __init__(self, name):
        self.name = name # <-- Instance Variables

angelo = Dog('Angelo')
white = Dog('White')
print (angelo.name, white.name)
print (angelo.num_legs, white.num_legs)
print (Dog.num_legs)
# print (Dog.name) # <-- this will cause error, you cant access instance var that way

'''
if you modified the class variables, all the variable of that class will get affected
'''
Dog.num_legs = '6'
print (angelo.num_legs, white.num_legs)
Dog.num_legs = '4'
white.num_legs = '6'
print (angelo.num_legs, white.num_legs, Dog.num_legs)
print (white.num_legs, white.__class__.num_legs) # class variable out of sync. white.num_legs created an instance var with the same name as clas var

class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances += 1 # shared with class variable:num_instances

print("everytime a new instance created with this class, it increments the share counter")
print(CountedObject.num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)


class BuggyCountedObject:
    num_instances = 0
    def __init__(self):
        self.num_instances += 1 # this use the instance variable. everytime intantiate will be assigned.

print('Buggy implementation of counted object')
print(BuggyCountedObject.num_instances)
print(BuggyCountedObject().num_instances) # each instance have their own num_instances, so they wont be able to accumulate
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject.num_instances)
