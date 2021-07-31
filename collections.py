# Collections
import collections
from collections import Counter

#Containers
#list
#dict
#tuple - immutable

#Types
#1 counter
#2 deque
#3 namedTuple()
#4 orderedDict
#5 defaultdict

a = Counter('gallad')
print(a)
b = Counter([1, 2, 3, 4, 5 , 6, 7, 8, 9])
print(b)
c = Counter({'a':1, 'b':2})
print(c)
d = Counter(cats=4, dogs=7)
print(d)
print(d['cats'])

print(list(d.elements()))

print(c.most_common(1))

e = Counter(a=4, b=2, c=0, d=2)
f = Counter(['a', 'b', 'b', 'c'])

""" e.subtract(f)
print(e)

e.update(f)
print(e)

e.clear()
print(e) """

#Operations
print(e+f)
print(e-f)
print(c & d)
print(c | d)
