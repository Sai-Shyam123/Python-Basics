import time

def func(f):
	def wrapper(*args, **kwargs):
		print('Started')
		rv = f(*args, **kwargs)
		print('Ended')
		return rv

	return wrapper

@func
def func2(x, y, z):
	print(x, y)
	return z

@func
def func3(a):
	print('I am func3')

func2(30, 'hello', 3)
func3(4)

## time ##

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rbv = func()
		total = time.time() - start
		print('Time: ' , total)
		return rbv
	return wrapper

@timer
def test():
	for _ in range(100000):
		pass

test()