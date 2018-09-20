#!/usr/bin/python
'''
list - mutable dynamic arrays (can be added or removed
'''
print('LIST EXAMPLE::')
arr = ['one', 'two', 'three']
print(arr[0])
print(arr)

print('list are mutable:')
arr[1] = 'Changed'
print(arr)

del arr[1]
print(arr)

print("list can hold arbitrary data types:")
arr.append(23)
print(arr)

'''
tuple - immutable containers (cant be removed or added, only can be defined at creation time)
'''
tuplearr = 'one', 'two', 'three'
print(tuplearr[0])
print(tuplearr)

'''
array.array - Typed Arrays, more space efficient compare to lists and tuples. Array stored are tightly packed.
useful when storing same type elements.
'''
from array import array
arr_arr = array('f', (1.0, 1.5, 2.0, 2.5))
print(arr_arr[1])
print(arr_arr)
print('array are mutable:')
arr_arr[1] = 23.0
print(arr_arr)
del arr_arr[1]
print(arr_arr)
arr_arr.append(44)
# arr_arr[1] = 'hello' # array are typed - TypeError: a float is required

'''
str - immutable arrays of unicode characters (in python 3.x)
str object are space-efficient bcause they are tightly packed and specialize in a single data-type. if you are storing unicode text,
you should use them. because str are immutable in python, modifying them requires creating a modified copy.
'''
arr_str = 'abcd'
print(arr_str[1])
print(arr_str)
print("String are immutable: ")
# arr_str[1] = 'e' # 'str' object doesnot support item deletion
print("String can be unpack into a list to get a mutable representation")
print(list(arr_str))
print(''.join(list(arr_str)))
print("String are recursive data structures: ")
print(type('abc'))
print(type('abc'[0]))

'''
bytes - immutable arrays of single bytes
similar to str objects. they are space-efficient, immutable, but unlike str, they are dedicated "mutable by array" data type called bytearray
that can be unpacked into.
'''
arr_byte = bytes((0, 1, 2, 3))
print(arr_byte[1])

# bytes literals have their own syntax:
print(arr_byte)
print(type(arr_byte))
