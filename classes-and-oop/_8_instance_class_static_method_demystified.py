#!/usr/bin/python

'''
Instance Method - regular instance method that is basic, no-frills method that will be use all time. Through the parameter self, instance
method can access attributes and other method of the same object. Instance method can also access the class itself through the self.__class__
attribute. This give instance method power to modify class state as well. Instance method cannot be called before being instatiate.

Class Method - This method is mark with @classmethod decorator to flag it as class method. Instead of accepting self param, class method take
a cls param that point to the class (not object instance) when method is called. Class method cant modify object instance state. Class method
able to make changes to the class state that applies access all instance of the class.

Static Method - mark with @staticmethod to flag it as static method. This method does not take self or cls param, although of course, it can
be made to accept and arbitrary number of other param. So as result, a static method cannot modify object nor class state. They are restricted
in what date they can access - they are primarily a way to namespace your methods.

Static methods and class methods are ways to communicate developer intent while enforcing that intent enough to avoid most 'slip of mind'
mistakes and bugs that would break the design.


'''

class MyClass:
    # Instance Method
    def method(self):
        return "instance method called", self

    # Class Method
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # Static Method
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method()) # when method is called, python replace self arg with instance of obj.
print(obj.classmethod())
print(obj.staticmethod())

print("accessing method with the class itself:")
print(MyClass.classmethod())
print(MyClass.staticmethod())
# print(MyClass.method()) #TypeError: unbound method method() must be called with MyClass instance as first argument (got nothing instead)
