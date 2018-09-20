#!/usr/bin/python
'''
Compared to arrays, record data structures provide a fixed number of fields, where each field can have a name and may also diff type.

in python, you could use dict as record data type or data object. Data object created using dict are mutable and there is a little
protection against misspelled field names, as fields can be added and removed freely at any time.
'''

car1 = {
    "color": 'red',
    "mileage": 3811.91,
    "automatic": True
}
car2 = {
    "color": 'red',
    "mileage": 40123,
    "automatic": False
}

# Dict have a nice repr:
print(car2)
print('Dictionary object are mutable')
car2["windshield"] = 'broken'
print(car2)

# no enforce on field naming, so no protection against wrong field name and missing/extra fields
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken'
}


'''
tuple - immutable groups of objects
Python's tuples are simple data structures for grouping arbitrary objects. Tuples are immutable - they cannot be modified once they created.
'''

car1_tuple = ('red', 3122, True)
car2_tuple = ('blue', 10239, False)
print(car1_tuple)
print(car2_tuple)
# no protection against missing/extra fields or wrong order:
car3_tuple = (34122, 'green', True, 'silver')

'''
Custom Class - More work, more control
classes allow you to define reuseable blueprint for data objects to ensure each object provides the same set of fields.
writing a custom class is a great option whenever you'd like to add business logic and behaviour to your object using methods. However,
this means that these objects are technically no longer plain data objects.
'''

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic
    def __str__(self):
        return "test"
custom_car1 = Car('red', 3812.1, True)
custom_car2 = Car('blue', 30812.1, False)
print(custom_car1.mileage)
custom_car1.mileage = 12
custom_car1.windshield = 'broken'
print(custom_car1)

'''
collections.namedtuple - convinient data objects. Immutable.
'''
from collections import namedtuple
from sys import getsizeof
p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)
print(getsizeof(p1))
print(getsizeof(p2))

# example of Car object implementation with namedtuple
NamedtupleCar = namedtuple('Car', 'color mileage automatic')
tcar1 = NamedtupleCar('red', 3812.13, True)
print tcar1
print 'Accessing Field: Mileage', tcar1.mileage


'''
typing.NamedTuple - improved namedtuples (added on python 3.6). very similar to namedtuple, main difference is the
updated syntax for defining new record types and added support for the type hints.

from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool
car1 = Car('red', 3812.4, True)
print(car1)
# >> Car(color='red', mileage=3812.4, automatic=True)

Fields are immutable
car1.mileage = 12 # Cause AttributeError: cant set attribute

Type annotation are not enforces without a seperate type checking tool like mypy:
Car('red', 'NOT_A_FLOAT', 99) # this will be valid which is not intended...
'''

'''
struct.Struct - Serialized C Structs
Converts between python values and C structs into python bytes objects. These are seldom used to represent
data objects meant to be inside python code, they are more intended as data exchange format rather than a way
of holding data in memory.
'''
