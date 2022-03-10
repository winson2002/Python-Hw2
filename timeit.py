import time

def calculate_time(func):
	def wrapper():
		start = time.time()
		stored = func()
		end = time.time()
		print('Total time ' + str(start - end))
		return stored
	return wrapper
