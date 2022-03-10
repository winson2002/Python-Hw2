def func_counter(func):
	def wrapper(y):
		wrapper.counter += 1
		return func(y)
	wrapper.counter = 0
	return wrapper
