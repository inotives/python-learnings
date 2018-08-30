#!/usr/bin/python

'''
Functions are objects
---------------------------------
Python functions are 1st-class objects. You can assign them to variables, store them in data structures,
pass them as arg to other function and even return them as value from other functions.
All data in a python program is represented by objects or relations between objects. Things like strings, lists,
modules, and functions are all objects.
'''

def yell(text):
    return text.upper() + '!'


def learning_functions_are_objects():
    print(yell("Hello all"))
    # the following line take the function object reference of yell() and create a second name bark that point to it.
    bark = yell
    print(bark("Woof"))

    #if you delete the yell, you could still access the same function through bark coz it is still point toward that func.
    # del yell
    # yell('hello?')
    # print(bark("woooofff"))

'''
Function can be stored in Data structures
--------------------------------------------
Since function are object, you can store them in data structures for example store them in a list.
To access them, it is the same way you access any other object type. You could also call a function store in the list
without assigning them to a variable.
'''
def learning_function_stored_in_data_struct():
    funcs = [yell, str.lower, str.capitalize]
    print funcs
    for f in funcs:
        print f, f('hey....')
    print funcs[0]("hey..yoyoyo")


'''
Functions can be passed to other functions
---------------------------------------------
Because functions are object, you can pass them as argument to other functions. This ability allow you to abstract away
and pass around behaviour in you program.
Function that accept other functions as arguments are also called higher-order-functions such as map function in python.
'''
def greet(func):
    greeting = func('Hi, i am a developers.')
    print greeting

def whisper(text):
    return text.lower() + '...'

def learning_functions_can_be_passed_to_other_functions():
    print greet(yell)
    print greet(whisper)
    print "example use of map func:"
    print list(map(yell, ["hihi", "hey", 'hello']))


'''
Function can be nested
------------------------
Python allow functions to be defined insided other functions. These are call nested function or inner function.
The inner function define in the function does not exist outside of the function.
In the case that you need to access the inner function, you return them via some conditioning.
'''
def speak(text):
    def whispering(t):
        return t.lower() + '...'
    return whispering(text)

def get_speak_func(volume):
    def whispering(text):
        return text.lower + '...'
    def yelling(text):
        return text.upper + '!'
    # this does not call the function, it is only return the inner function base on the conditioning.
    if(volume > 0.5): return yelling
    else: return whispering

def learning_function_can_be_nested():
    print speak('Hello, world')
    # print whispering('this will be errored') #NameError: global name 'whispering' is not defined
    # print speak.whisper #AttributeError: 'function' object has no attribute 'whisper'

'''
Function can capture local state
---------------------------------
The inner functions can also capture and carry some of the parent function's state with them.
Inner function able to do this because of lexical closures. A close remembers the values from its enclosing lexical scope.
In practical terms, this means not only can functions return behaviours but they can also pre-configure those behaviours.
Below example of make_adder serves as factory to create and configure 'adder'.
'''
def make_adder(n):
    def add(x):
        return x+n
    return add

def learning_function_can_capture_local_state():
    plus_3 = make_adder(3)
    plus_4 = make_adder(4)

    print "make use of function to make a factory function that remember the state configure"
    print plus_3, plus_3(4)
    print plus_4, plus_4(10)


'''
Object can behave like functions
------------------------------------
while all function are objects in python, the reverse is not true. object arent functions.
But they can be make callable which allow you to treat them like function in many caseself.
If an object is callable it mean you can use the round parentheses function call syntax on it and
even pass in function call arguments. This is all powered by the __call__ dunder method.
Not all object are callable, to check, you can use the built-in `callable` function.
'''
class Adder:
    def __init__(self, n):
        self.n = n

    #when the object is called, it will run this __call__ function block.
    def __call__(self, x):
        return self.n + x

def learning_obj_behave_like_function():
    plus_3 = Adder(3)
    print plus_3, "callable?" + str(callable(plus_3)), plus_3(10)





def main():
    learning_obj_behave_like_function()

if __name__ == '__main__':
    main()
