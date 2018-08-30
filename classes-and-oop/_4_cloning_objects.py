#!/usr/bin/python

'''
Shallow Copy
-------
Constructing new collection of objects and then populating it with references to the child objects found in the original.
This mean it is only 1-level deep which the copying process does not recurse and child objects copies wont be created.
'''

xs = [[1,2,3], [4,5,6], [7,8,9]]
ys = list(xs) # make a shallow copies

print "XS:", (xs)
print "YS:", (ys)

print "adding sublist to XS"
xs.append(["New Item"])

print "XS:", (xs)
print "YS:", (ys)

print "but because the child reference of YS is the same as XS, if changes was made to XS child object, YS will get affected."
xs[1][0] = 'X'
print "XS:", (xs)
print "YS:", (ys)


'''
Deep Copy
-------
Deep copy makes the copying process recursive. First construct a new collection object then recursively populate it with
the copies of the child object found in the original. The result copied object will be a complete independent copies.
'''

print "\n\nDEEP COPY Example"
import copy
xa = [[1,2,3], [4,5,6], [7,8,9]]
za = copy.deepcopy(xa)
print "XA:", xa
print "ZA:", za
print "with deepcopy, if changes was made to XA, ZA wont get affected."
xa[1][0] = "XX"
print "XA:", xa
print "ZA:", za
