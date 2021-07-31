import inspect
from queue import Queue as q

class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person({self.name})'

	def __mul__(self, x	):
		if type(x) is not int:
			raise Exception('Invalid arguement, must be int')
		self.name = self.name*x

	def __call__(self, y):
		print('called this function ', y)

	def __len__(self):
		return  len(self.name)

p = Person("SaiShyam")
# p * 4
print(len(p))

############

# q = Queue()
# print(q)

class Queue(q):
	def __repr__(self):
		return f'Queue({self.qsize()})'

	def __add__(self, item):
		self.put(item)

	def __sub__(self, item):
		self.get()
qu = Queue()
qu + 'hello'
qu + 123
qu - None
print(qu)