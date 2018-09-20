#!/usr/bin/python

print ">> EXAMPLE:: Looping in Python ------------>>"
my_item = ["a", "b", "c"]
for i, item in enumerate(my_item):
    print "%s: %s" % (i, item)

emails = {
    'Bob': 'bob@example.co',
    'Alice': 'alice@sample.co'
}
for name, email in emails.items():
    print "%s -> %s" % (name, email)


'''
Python Comprehensions
-----------------------
The key to understand list Comprehensions is that they are just for-loops over a collection but expressed in a more terse and compact syntax.
FORMAT :>>  values = [ expression for item in collection <if condition> ]
'''
print ">> EXAMPLE:: Python Comprehensions ------------>>"
print "[LIST] Squaring:", [x * x for x in range(10)]
print "[LIST] Squaring (only even num):", [x * x for x in range(10) if x % 2 == 0] # filtering the collection
print "[SET] Squaring: ", {x * x for x in range(-9, 10)} # set are unordered and no duplicates
print "[DICT] Squaring:", { x: x * x for x in range(5) } # dict comprehensions

'''
Python List Slicing
--------------------
FORMAT :>> [start:stop:step] default step=1
'''
print ">> EXAMPLE:: List Slicing ------------>>"
lst = [1,2,3,4,5]
copylst = lst
print lst
print lst[1:3:1]
print lst[1:3]
print lst[::2]
print lst[::-1] # with [::-1] you will get the reverse order (only for numbers)
del lst[:] # this will empty the whole list (refrence pointing to this list also will get updated)
print lst, copylst

'''
beside clearing list, you can also use slicing to replace all elements of a list without creating a new list object.
This is a nice shorthand for clearing a list and then repopulating it manually
'''
lst = [1,2,3,4,5]
original_lst = lst
lst[:] = [7,8,9]
print 'lst:',lst
print 'original_lst', original_lst
print 'original=lst :', original_lst is lst
print 'another version, creating shallow copy'
copied_lst = lst[:]
print 'copied_lst:', copied_lst
print 'copied=lst :', copied_lst is lst


'''
Simple Iterator Class
'''
print ">> Simple Iterator Example ---------------->>"
class Repeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    # in Python3
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

    # in Python2
    def next(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = Repeater('Hello', 3)
for item in repeater:
    print(item)


'''
`yeild` - with this keyword as control flow, you could stop the execution of the functions.
'''
print ">> yield keyword usage example ------------------- >>"
def repeat_3_times(value):
    yield value
    yield value
    yield value

# More than the yield declared, StopIteration Error occur.
for x in repeat_3_times('should stop after - 3'): print x

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
for x in bounded_repeater('Hello', 5): print x
