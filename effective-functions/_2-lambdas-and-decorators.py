#!/usr/bin/python

'''
Lambdas are single-expression functions
----------------------------------------
`lambda` is use to declare small anonymous functions. they behave like `def` and can be used whenever function obj are required.
using lambda, we dont need to bind function to object before we use it.
Lambdas are restricted to a single expression. lambda function cant use statements or annotation.

Lambda should be use sparingly and with extra care. Lambda is meant for simple concise expression, if you feel like
you create a complex expression with lambda, you are using it wrongly and sometime might be harmful.
'''

def learning_lambdas():
    print "Simple lambdas: ", (lambda x, y: x + y)(5,3)
    print "Example of using lambda in sorting:"
    data = [(1, 'd'), (2, 'n'), (4, 'f'), (3, 'c')]
    # sort the array base on the 2nd value in each tuple
    print sorted(data, key=lambda x: x[1])
    print sorted(range(-5, 6), key=lambda x: x * x)

'''
Python Decorator
-----------------
Python's decorators allow you to extend and modify the behaviour of a callable(functions, methods and classes)
without permanently modifying the callable itself.
Some usage for decorator:
 - logginf
 - enforcinf access control and auth
 - instrumentation and timing functions
 - rate-limiting
 - caching and more...

in basic term: a decorator is a callable that takes a callable as input and returns another callable.
putting `@syntax` line in front of the function definition is the same as defining the function first then running
through the decorator.
Multiple decorators can be applied as well. Order of the decorators were applied: `from bottom to top`. This behaviour can be
called decorator stacking.
'''
def null_decorator(func):
    print 'decorator 1st'
    return func

# this decorator convert text to uppercase
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() +'</em>'
    return wrapper

# how to applied decorator
@strong
@emphasis
@uppercase
def greet():
    return 'Hello'


def learning_decorator_1():
    print greet()

'''
Decorator function that accept arguments
-----------------------------------------
In order to make decorator function to take in argument, you will need *args and **kwargs feature from python which will come in handy.

'''
def proxy(func):
    # * and ** operators in the wrapper closure to collect all positional and keywords argu and store in var (args & kwargs)
    def wrapper(*args, **kwargs):
        # forward the collected arguments to original input function using * and ** "argument unpacking" operators
        return func(*args, **kwargs)
    return wrapper

'''
For example the below trace decorator that logs function arguments and result during execution time.
'''
def trace(func):
    def wrapper(*args, **kwargs):
        print "TRACE: calling", func.__name__, "() with", args, kwargs
        original_result = func(*args, **kwargs)

        print "TRACE: ", func.__name__, "() returned", original_result
        return original_result
    return wrapper

@trace
def say(name, line):
    return name + ": " + line

'''
as a debugging best practice, use the functools.wraps() helper in your own decorators to carry over metadata from
the undecorated callable to the decorated one.
Decorators are not a cure-all and should not be overused. it is important to balance the need to get stuff done with
the goal of not getting tangled up in a horrible unmaintainable mess of a code base.
'''

def learning_decorator_2():
    print say('Jane', 'Hello World')

'''
More fun stuff with *args and **kwargs
----------------------------------------
*args and **kwargs allow a function to accept optional arguments, so you can create flexible APIs in your modules and classes.
*args - collect extra positional arguments as a tuple (actual syntax *)
**kwargs - collect extra keywords arguments as a dictionary (actual syntax **)
Both args and kwargs can be empty if no extra arguments are passed to the function.

it is possible to pass optional or keyword parameters from one function to another by using the argument-unpacking operators
* and ** when calling the function you want to forward your arguments to. This also give you opportunity to modify the
argument before pass them along. This technique can be useful for subclassing and writting wrapper functions. You could use
this to extend the behaviour of parent class without having to replicate the full signature of its constructor in child class

'''

def foo(required, *args, **kwargs):
    print required
    if args:
        print args
    if kwargs:
        print kwargs

def bar(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra',)
    foo(x, *new_args, **kwargs)

import functools
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print 'inside decorated_function'
        print f, args, kwargs
        print f(*args, **kwargs) # this function was the function wrapped by trace
    return decorated_function

# when running this, greet2() will be wrapped by trace function.
@trace
def greet2(grt, name, **kwargs):
    return '{}, {} !!!'.format(grt, name)

'''
Another usage of * and ** are for unbpack function arguments from sequences and dictionary.
'''
def print_vector(x, y, z):
    print "<%s %s %s>" % (x, y, z)

def learning_fun_stuff_with_args_and_kwargs():
    foo("hello")
    print "called with *args: \n--------------------"
    foo("hello", 1, 2, 3)
    print "called with both *args and **kwargs: \n--------------------"
    foo("hello", 1, 2, 3, key1="val", key2=999)
    print("just the **kwargs: \n--------------------")
    foo("hello", key1="val", key2=999)

    print ("Passing the *args and **kwargs")
    bar("hello", 12,13, key1="something", key2=123)

    print "greet2() will be wrapped by trace(): "
    greet2('hello', 'bob', key1=1, key2=2)

    print "use * for unpacking sequences in list:"
    print_vector(0, 1, 0)
    tuple_vec = (1, 0, 1)
    list_vec = [1, 0, 1]
    print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
    print "a better way to do:"
    print_vector(*tuple_vec)
    print_vector(*list_vec)
    genexpr = (x * x for x in range(3))
    print_vector(*genexpr)
    print "example of unpacking keyword argument"
    dict_vec = {'x': 0, 'y': 1, 'z': 1}
    print_vector(**dict_vec)
    print "if you wan to obtain the key instead of the value"
    print_vector(*dict_vec)

'''
Python Return
----------------
Python add an implicit return None statement at the end of any function. so any function will return none by default.
def return1(value):
    if value: return value
    else: return None

def return2(value):
    if value: return value
    else: return

def return3 (value):
    if value: return value
'''





def main():
    learning_fun_stuff_with_args_and_kwargs()

if __name__ == '__main__':
    main()
