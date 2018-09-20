#!/usr/bin/python
'''
a stack is a colection of objects that supports fast last-in, first-out (LIFO) semantics for insert and deletes. Unlike lists or arrays,
stacks typically dont allow for random access to the object they contain. They use the `push` and `pop` to insert and delete.
queue and stack are quite similar. They are both linear collections of items with the only difference in the order item are accessed.

queue - first-come, first-out (FIFO)   <VS>  stack - last-in, first-out (LIFO)

push in _                                           push in _ pop _ out
        _                                                   _
        _                                                   _
        _                                                   _
        pop _ out

In python, the built in list type makes a decent stact data structure as support push pop operation.
'''
print "-------------- Stacks ----------------"
print "USING LIST TO MAKE STACK:"
s = []
s.append('push1') # push for list
s.append('push2')
s.append('push3')
print s
print "Pop: %s" % s.pop()
print s
s.append('push4')
print s

'''
collections.deque - Fast & Robust Stacks
the deque class implements a double-ended queue that supports adding and removing elements from either end. Because deques support adding
and removing elements from either end equally wells, they can serve as both queues and stacks.
'''
print "USING DEQUE TO MAKE STACK:"
from collections import deque
ds = deque()
ds.append('push1')
ds.append('push2')
ds.append('push3')
print ds
print "Pop: %s" % ds.pop()
print ds
ds.append('push4')
print ds

'''
Queue.LifoQueue - Locking Semantics for parallel computing (in python3, instead of Queue, use queue)
This stack implementation in python standard library is synchronized and provides locking semantics to support multiple concurrent
producers and consumers. Beside LifoQueue, inside the Queue class, there are other implementation using multi-producer/multi-consumer queue
that are useful for parallel computing.
Depending on the use case, the locking semantics might be helpful or they might incur unneeded overhead.
It is better off to use a list or a deque as general purpose stack.
'''
print "USING LIFOQUEUE TO MAKE STACK:"
from Queue import LifoQueue
ls = LifoQueue()
ls.put('put1')
ls.put('put2')
ls.put('put3')
print ls
print "Pop: %s" % ls.get()
print "Pop: %s" % ls.get()
print "Pop: %s" % ls.get()
# print lq.get_nowait() # raise Queue.Empty
# print lq.get() # Blocks / wait forever

print "-------------- Queues ----------------"
'''
list - Terribly Slow implementation of Queues
In order to make list into queue, you will need to shift all the other element by one - O(n) time.
'''
print "USING LIST TO MAKE QUEUE:"
q = []
q.append('push1')
q.append('push2')
q.append('push3')
print q
print "Pop: %s" % q.pop(0) # this is extreme slow - ok for small set, but super slow for big data sets, speed: O(n)
print q

'''
collections.deque - Fast & Robust Queues
This is a great default choice if you are making queue
'''
print "USING DEQUE TO MAKE QUEUE:"
dq = deque()
dq.append('push1')
dq.append('push2')
dq.append('push3')
print dq
print "Pop: %s" % dq.popleft()
print "Pop: %s" % dq.popleft()
print dq

'''
multiprocessing.Queue - Shared Job Queue
Which allow queued items to be processed in parallel by multiple concurrent workers. As specialized queue implementation meant for sharing
data between  processes, multiprocessing.Queue makes it easy to distribute work accross multiple processes in order to work around the
Global Interpreter Lock (GIL) limitations. This type of queue can store and transfer any pickle-able object accross boundaries.
'''
from multiprocessing import Queue
mq = Queue()
mq.put('eat')
mq.put('sleep')
mq.put('code')
print mq
print mq.get()
print mq.get()
print mq.get()



'''
Priority Queue is a container data structures that manages a set of records with totally-ordered key (e.q. numberic weigthed value) to
provide quick access to record with the smallest or largest key in the set.
In a gist - Priority Queue - queue that retrieve elements base on their priority.
Priority queue usually used in dealing with scheduling problem, for e.q. to give precedence to tasks with higher urgency.

'''
print "-------------- Priority Queues ----------------"
print ">> PRIORITY QUEUE with LIST::"
pq = []
pq.append( (2, 'code') )
pq.append( (1, 'eat') )
pq.append( (3, 'sleep') )
print "unsorted:", pq
pq.sort(reverse=True) # remember to re-sort everytime a new element is inserted or use bisect.insort()
print "sorted:", pq
while pq: print pq.pop() # pop all the item in the pq list

'''
heapq - List-Based Binary Heaps
This is a binary heap implementation usually backed by a plain list, and it supports insertion and extraction of the smallest element in
O(log n) time. This is a good choice for implementing priority queues in Python. Since heapq technically only provides a min-heap
implementation, extra steps must be taken to ensure sort stability and other features typically expected from a practical priority queue.
'''
print ">> PRIORITY QUEUE with heapq::"
import heapq
hpq = []
heapq.heappush(hpq, (2, 'code'))
heapq.heappush(hpq, (1, 'eat'))
heapq.heappush(hpq, (3, 'sleep'))
print hpq
while hpq: print heapq.heappop(hpq)

'''
queue.PriorityQueue - Beautiful Priority Queue
This implementation uses heapq internally and shares the same time and space complexities. The difference is that PriorityQueue is
synchronized and provides locking semantics to support multiple concurrent producers and consumers.
'''
print ">> PRIORITY QUEUE with Queue.PriorityQueue::"
from Queue import PriorityQueue
qq = PriorityQueue()
qq.put( (2, "code") )
qq.put( (1, "eat") )
qq.put( (3, "sleep") )
print qq
while not qq.empty(): print qq.get()
