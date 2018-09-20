#!/usr/bin/python
'''
Dictionaries are central data structures which store an arbitrary number of objects, each identified by an unique dict key.
Dict are also called maps, hashmaps, lookup tables or associated arrays. They allow for efficient lookup, insertion and deletion of
any object associated with a given key.

In python, one of the way to create a dict object is thru the use of curly-braces.
'''

phonebook = {
    'bob': 9112930123,
    'ada': 1920399123,
    'mic': 4942931233
}
squares = {x: x * x for x in range(6)}
print(phonebook)
print(squares)

'''
collections.OrderedDict - dict that remember te insertion order of the keys.
'''
from collections import OrderedDict
d = OrderedDict(one=1, two=2, three=3)
print(d)
d['four']=4
print(d)
print(d.keys())

'''
collections.defaultdict - return default values of missing keys
'''
from collections import defaultdict
dd = defaultdict(list)
dd['dogs'].append('Ruff')
dd['dogs'].append('Maya')
dd['dogs'].append('Mio')
dd['dogs'].append('Bak')
print(dd)
print(dd['dogs'])

'''
collections.ChainMap - search multiple dictionaries as a single mapping only. (only in python3.3 onward)

from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
print(chain)
>> ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
print(chain['one'])
>> 1
print(chain['three'])
>> 3
'''

'''
types.MappingProxyType - a wrapper for making read-only dictionaries (only in python3.3 onward)

from types import MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])
>> 1
read_only['one'] = 23
>> TypeError: "mappingproxy" object does not support item assignment

# updates to the original are reflected in the proxy:
writable['one'] = 42
print(read_only)
>> mappingproxy({'one': 42, 'two': 2})
'''
