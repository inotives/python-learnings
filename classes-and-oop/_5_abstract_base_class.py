#!/usr/bin/python

'''
Abstract base classes ensure that derived classed implement particular methods from base class.

'''

class Base:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return "foo() called"
    # forgot to override bar()
    # def base(self):
    #     return "bar() called"

c = Concrete()
print (c.foo())
# print (c.bar()) # this will cause error - NotImplementedError inherit from Base class
