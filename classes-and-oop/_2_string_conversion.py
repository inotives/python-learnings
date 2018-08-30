#!/usr/bin/python

'''
in python, there are ways to convert string in different situation by using __str__ and __repr__ dunders.
__str__ dunders get called when you try to convert an object into a string through the following means:
    > print(obj)
    > str(obj)
    > "{}".format(obj)
__repr__ dunders is what the class go for when in interpreter session.

If you dont add a __str__ method, python falls back on the result of __repr__ when looking for __str__.
So it is recommended that you always add at lease a __repr__ method to your classes. This will guarantee a
useful string conversion result in almost all cases.

'''

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "__str__ of a %s car" % (self.color)

    # return the object at the interpreter session
    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.color, self.mileage)

my_car = Car("RED", 12345)
print my_car
print str(my_car)
print "{}".format(my_car)

print repr(my_car)
