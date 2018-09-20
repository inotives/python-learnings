#!/usr/bin/python

'''
python's tuples are simple data structures for grouping arbitrary object and they are immutable (cannot modified once created).
data stored in tuples can only be access by accessing through integere indexes (e.q tup[2]).

Nametuples can be count as the extension to python tuples. Nametuples are immutable containers just like normal tuples.
Each nametuples are named/index with human readable unique identifier.

Namedtuples can be an easy way to clean up your code and make it more readable by enforcing better structures for your data.

'''

tup = ('hihya', object(), 55)
print (tup)
print (tup[2])
# tup[2] = 22 # TypeError: 'tuple' object does not support item assignment

# example of Nametuples
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 8199.23)
print(my_car.color, my_car[1])
print(tuple(my_car))
# tuple unpacking and the *-operator for function argument unpacking also work as expected.
color, mileage = my_car
print(color, mileage)
print( my_car )
# my_car.color = 'blue' # AttributeError: Cant set attribute - due to namedtuple being immutable

'''
Subclassing Namedtuples -  since they are build on top of regular python classes, you can even add method to namedtuple.
The easiest way to create hierarchies of namedtuple is to use the base tuple's _fields property
'''

class MyCarWithMethods(Car):
    def hexcolor(self):
        return "#FF0000" if self.color == 'red' else "#000000"

c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

# using base tuple field then add new immutable fields
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
ec = ElectricCar('red', 1112.32, 46.12)
print (ec)

import json
print (my_car._asdict() ) # helper-method: return namedtuple as dictionary
print (json.dumps(my_car._asdict())) # this is good when use to output json to avoid typos

print (my_car._replace(color = 'blue')) # helper-method(_replace): create a shallow copy & allow you to replace selective fields
print (my_car._make(['yellow', 192])) # helper-method(_make): create new instances of a namedtuple from a sequence of iterable
