#!/usr/bin/python

'''
The `==` operator compares by checking for equality.
the `is` operator compares identities
'''

a = [1, 2, 3]
b = a

print a == b, " - a list is the same as b list, value in the content are the same."
print a is b, " - a object is b object / a point to the same object as b"

# create identical copy of list object of a
c = list(a)
print a == c, " - a list is the same as b list, value in the content are the same."
print a is c, " - a object NOT the same as b object, they point to different object."
