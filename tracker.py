def func_counter(func):
	def wrapper():
		wrapper.counter += 1
		return func()
	return wrapper
