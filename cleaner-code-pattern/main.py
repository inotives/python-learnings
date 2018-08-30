#!/usr/bin/python

'''
1. Assertion
----------------------
ASSERT SYNTAX: assert <expression-1> [, <expression-2>]
Details:
Assertion is to inform developers about unrecoverable errors in a program. It is not intended to signal expected error conditions,
like File-Not-Found Error where user can take a corrective action or just try again.
Assertion are meant to be internal self-checks for your program by declaring some conditions as impossible in your code.
if one of these conditions doesn't hold, that mean there's a bug in the program. This is more of a debugging aid, not a mechanism to
handle the run-time errors.

Some common pitfall with using assertion:
1. Dont use Asserts for Data Validation
Assert can be globally disabled in python with -O or -OO command line as well as PYTHONOPTIMIZE env var in CPython.
If your program uses asserts to check if a function arg contain a wrong or unexpected value, this can be backfire quickly and
lead to bugs or security holes. for example:
   assert user.is_admin() #if assert was disabled, any user can delete the products.
   assert store.has_product(prod_id) #if assert was disabled, deletion of unknown prod_id usually will result in db hang

2. Assert that never fail
Becareful when writing multi line assertion. Sometime the syntax might cause the assertion to evaluate as always true.

'''
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    # this assertion make sure that the price cannot be lower than 0 and cannot be higher that original price of the product
    assert 0 <= price <= product['price'], 'Failed Price Assertion. Illogical'
    return price

def learning_assertion():
    print ('Learning Asserting Example: ')
    shoes = {'name':'Adidas - Neo Edition', 'price': 14900}
    print("Using asserting to assert the correctness of price: ", apply_discount(shoes, 0.25))
    print("if the assertiong failed: ", apply_discount(shoes, 2.5))
''' -- End ------------------------------------------------------------------------------------------------------------------ '''


'''
2. with statement and context manager
-----------------------------------------
with statement help simplify some common resource management pattern by abstracting their functionality and allowing them to be
factored out and reused. for example:

   with open('hello.txt', 'w') as f:
       f.write('hello, world !!')

  can also be written as:
  f = open('hello.txt', 'w')
  try:
      f.write('hello, world !!')
  finally:
      f.close()

you can provide the same functionality (like open() ) for your own classes and function by implementing `context managers`
Context Manager is a simple `protocol`(or interface) that your object need to follow in order to support the with statement.
All you need to do is add __enter__ and __exit__ methods to an object if you wan it to function as context manager.

'''

class ManagedFile:
    def __init__(self, name):
        self.name = name

    # when execution reach here, it will acquire the resource
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    # when execution reach here, it will free up the resource
    def __exit__(self, exc_type, ext_val, exc_tb):
        if self.file:
            self.file.close()

'''
The above ManageFile class can be written using contextlib module to define a generator-base factory function.
'''
from contextlib import contextmanager

@contextmanager # decorator & generator in python
def manage_file(name):
    try:
        # 1st acquire the resouces
        f = open(name, 'w')
        # next it temporarily suspend the its own execution and yields the resources so it can be use by the caller.
        yield f
    # when caller leave the context, the generator continue to execute the steps and resource can be release back to system
    finally:
        f.close()

def learning_context_manager(choice=1):
    print ("Learning Context Manager. Open up hello.txt to see. Default to choice: ", choice)
    if(choice == 1):
        with ManagedFile('hello.txt') as f:
            f.write('This text is written with Class ManageFile.')
            f.write('Bye now')

    elif(choice == 2):
        with manage_file('hello.txt') as f:
            f.write("Replaced by manage_file function.")
            f.write("bye bye.")
    else: print('please choose a choice of 1 or 2')

'''
Using `with` effectively can help you avoid resource leaks and make your code easier to read.

-- End -----------------------------------------------------------------------------------------------------------------------
'''

'''
3. Underscores, Dunders and More
-----------------------------------------

>> Single Leading Underscore: `_var`
The single leading underscore is just a standard for programmer use. It mean the variable/function is intended for internal use.
But this is just an agreed-convention, it does not prevent others from accessing the variable out side of the class.
However, leading underscore do impact how names get imported from modules. e.q:

from my_module import *
external_func()
_internal_func()
NameError: 'name ' _internal_func is not defined.

   instead do this to avoid:

import my_module
my_module.external_func()
my_module._internal_func()


>> Single Trailing Underscore: `var_`
It is used convention to avoid naming conflicts with python keywords.


>> Double Leading Underscore: `__var` or call it `dunders`
a double underscore prefix causes the python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclass.
It is called name mangling. The interpreter changes the name of the var in a way that makes it harder to create collisions when the class
is extended later.

'''

_ManglingTest__mangledglobal = 'Mangled-Global'
class ManglingTest:
    def __init__(self):
        self.__mangled  = 'hello'
    def get_mangled(self):
        return self.__mangled
    def get_mangled2(self):
        return __mangledglobal

    def __method(self):
        return 42
    def call_it(self):
        return self.__method()

'''
>> Double Leading and Trailing Underscore: `__var__`
Variables surrounded by a double underscore prefix and postfix are left unscathed by python interpreter when name mangling happened.
However there are some name that have both leading and trailing double underscore that are reserved like __init__ for object construct,
or __call__ to make object callable.


>> Single Underscore: `_`
per convention, a single stand-alone underscore is sometimes used as a name to indicate that a var is temporarily or insignificant.
This also represent the result of the last expression in python REPL Session.
'''

def learning_underscore_dunder_mangling():
    print "Name Mangling Example:"
    print "called the var in class by get function you will see `hello`. Output::", ManglingTest().get_mangled()
    # print("called the __var directly, will get you error. ", ManglingTest().__mangled)
    print "called the method in class by function: ", ManglingTest().call_it()
    # print("called the method directly: ", ManglingTest.__method() )
    print "called the var __mangledglobal via get function:", ManglingTest().get_mangled2()


'''-- End -----------------------------------------------------------------------------------------------------------------------'''


from string import Template
def learning_string_formatting():
    errno = 50159747054
    name = 'Bob'

    print "Hey %s, there is a 0x%x error!" % (name, errno)
    print "Hey %(name)s, there is a 0x%(errno)x error!" % {"name": name, "errno": errno}
    print "Hello, {}" .format(name)
    print "Hey {name}, there is a 0x{errno:x} error!" .format(name=name, errno=errno)

    # Using Template Module
    t = Template("Hey, $name!")
    print t.substitute(name=name)
    templ_string = "Hey $name, there is a $errno error!"
    print Template(templ_string).substitute(name=name, errno=hex(errno))

    



def main():
    # learning_assertion()
    # learning_context_manager()
    # learning_underscore_dunder_mangling()
    learning_string_formatting()


if __name__ == '__main__':
    main()
