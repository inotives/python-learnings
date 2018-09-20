#!/usr/bin/python
'''
A set is an unordered collections of object that does not allow duplicate elements. In python, you could use curly-braces
set expression syntax and set comprehensions to conviniently define a new set instances. But becareful, to create an empty set,
you will need to call `set()` constructor. Using empty curly-braces is ambiguous and will create an empty dictionary instead.

'''

#Example of set instances with curly braces
vowels = {"a", "e", "i", "o", "u"}
print vowels
squares = { x * x for x in range(10) }
print squares
not_a_set = {}
print type(not_a_set)
empty_set = set()
print empty_set

print 'e' in vowels
letters = set('alice')
print letters.intersection(vowels)
vowels.add('x')
print vowels
print len(vowels)

'''
frozenset - Immutable Sets
immutable version of sets which could not be changes after creation.
'''
frozenset_vowels = frozenset({"a", "e", "i", "o", "u"})
# frozenset are hashable and can be used as dictionary keys:
d = {frozenset({1,2,3}): 'hello'}
print d
print d[frozenset({1,2,3})]



'''
collections.Counter - multisets (bag), type that allow elements in the set to have more than one occurence.
This is useful if you need to keep track of not only if an element is part of a set, but also how many times it is included in the set.
'''
print "MULTISET - Example"
from collections import Counter
inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print inventory
more_loot = {'sword': 4, 'apple': 2}
inventory.update(more_loot)
print inventory

print 'Total Unique Item set: %s' % len(inventory)
print 'Total of ALL items in the set: %s' % sum(inventory.values())
