def func_counter(func):
	def wrapper():
		wrapper.counter += 1
		return func(y)
	wrapper.counter = 0
	return wrapper
