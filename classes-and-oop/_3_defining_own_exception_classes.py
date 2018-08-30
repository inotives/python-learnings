#!/usr/bin/python

'''
Making your own error types can be of great valus as you could make the potential error case stand out clearly.
This will make your functions and modules become more maintainable. Custom error types also could be use to provide
additional debugging information.

Derive your custom exception from python built-in Exception class or from more specific exception classes like ValueError / KeyError
You can also use inheritence to define logically grouped exception hirachies.
'''

class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    def __str__(self):
        return "Name too Short"
    pass

class NameTooLongError(BaseValidationError):
    def __str__(self):
        return "Name too Long"
    pass


# Simple example:
def validateName(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    if len(name) > 20:
        raise NameTooLongError(name)

try:
    validateName('joe')
except BaseValidationError as err:
    print err

try:
    validateName('joelausneautopausilationalaiton')
except BaseValidationError as err:
    print err
