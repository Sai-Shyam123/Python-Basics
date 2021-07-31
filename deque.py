# Collections Deque
import collections
from  collections import deque

d = deque('hello')
d.append('4')
d.append(5)
d.appendleft('yoo ')
d.pop()
d.popleft()
print(d)
d.clear()
print(d)
d.extend('456')
d.extend('hello')
d.extendleft('hey')
print(d)
d.rotate(-1)
